from pydantic import BaseModel
from typing import List


class Predictions(BaseModel):
    predictions: List[float]