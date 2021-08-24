import re
import spacy


def get_top_words_per_topics(model, vocabulary, n_top_words=10):
    top_words = [] 
    for topic in model.components_:  # word distribution per topic 
        top_words.append([vocabulary[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
    
    return top_words


def preprocess(nlp, text):
    text = text.lower()
    text = text.strip()
    text = re.sub('\d', '', text)  # remove numbers 
    text = ' '.join(text.split())  # replace whitespace with single space

    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    tokens = [token for token in tokens if len(token) > 1]

    return ' '.join(tokens)