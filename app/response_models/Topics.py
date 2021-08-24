from pydantic import BaseModel
from typing import List


class Topics(BaseModel):
    topics: List[list]