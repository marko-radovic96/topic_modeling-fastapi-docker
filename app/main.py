from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseSettings
import pickle
from src.utils import get_top_words_per_topics, preprocess
from response_models.Topics import Topics
from response_models.Predictions import Predictions
import spacy


class Settings(BaseSettings):
    model_name: str = "Topic Modeling API"
    model_path: str = './pickle/model.pkl'
    vectorizer_path: str = './pickle/vectorizer.pkl'

settings = Settings()

app = FastAPI(title=settings.model_name,
              description="Topic Modeling API",
              version="1.0.0", )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=404,  # todo: does for every error server returns 404?
        content={"message": str(exc)},
    )


with open(settings.model_path, 'rb') as file:
    model = pickle.load(file)

with open(settings.vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

vocabulary = vectorizer.get_feature_names()

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
#C:\\Users\\Marko\\source\\repos\\python\\env\\Lib\\site-packages\\en_core_web_sm\\en_core_web_sm-3.1.0

@app.get("/topics", response_model=Topics, description="Returns n top words per topic",
         tags=["Topics"])
async def get_topics(num_of_words: int = 5):
    top_words = get_top_words_per_topics(model, vocabulary, num_of_words)
    return Topics(topics=top_words)


@app.get("/predict", response_model=Predictions, description="Returns topic probabilities for given text",
         tags=["Predict"])
async def predict(text: str = ''):
    text = preprocess(nlp, text)
    term_freq = vectorizer.transform([text])

    output = model.transform(term_freq)
    return Predictions(predictions=output[0].tolist())
    
