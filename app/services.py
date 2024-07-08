from typing import List

from fastapi import HTTPException

from app.schemas import Movie

movies = [
    Movie(
        **{
            "title": "Oppenheimer",
            "release_year": 2023,
            "genre": "Drama",
            "director": "Christofer Nolan",
            "famous_actors": [
                "Cillian Murphy",
                "Emily Blunt",
                "Matt Damon",
                "Robert Downey Jr.",
            ],
        }
    ),
    Movie(
        **{
            "title": "The Shawshank Redemption",
            "release_year": 1994,
            "genre": "Drama",
            "director": "Frank Darabont",
            "famous_actors": ["Tim Robbins", "Morgan Freeman"],
        }
    ),
    Movie(
        **{
            "title": "The Godfather",
            "release_year": 1972,
            "genre": "Crime",
            "director": "Francis Ford Coppola",
            "famous_actors": ["Marlon Brando", "Al Pacino"],
        }
    ),
]


def get_movies(skip: int = 0, limit: int = 10) -> List[Movie]:
    return movies[skip : skip + limit]


def get_movie_by_title(title: str) -> Movie:
    for movie in movies:
        if movie.title == title:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


def create_movie(movie: Movie) -> Movie:
    for m in movies:
        if m.title == movie.title:
            raise HTTPException(status_code=400, detail="Movie already exists")
    movies.append(movie)
    return movie


def delete_movie(title: str) -> Movie:
    for index, movie in enumerate(movies):
        if movie.title == title:
            deleted_movie = movies.pop(index)
            return deleted_movie
    raise HTTPException(status_code=404, detail="Movie not found")
