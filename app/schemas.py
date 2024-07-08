from typing import List

from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    release_year: int
    genre: str
    director: str
    famous_actors: List[str]
