from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_movies():
    response = client.get("/movies")
    assert response.status_code == 200


def test_create_movie():
    response = client.post(
        "/movies",
        data={
            "title": "Inception",
            "release_year": 2010,
            "genre": "Sci-Fi",
            "director": "Christopher Nolan",
            "famous_actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
        },
    )
    assert response.status_code == 200


def test_movie_form():
    response = client.get("/movies/form")
    assert response.status_code == 200


def test_get_movie_detail():
    response = client.get("/movies/Inception")
    assert response.status_code == 200


def test_delete_movie():
    response = client.delete("/movies/Inception")
    assert response.status_code == 200
