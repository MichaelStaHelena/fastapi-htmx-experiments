from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import Movie
from app.services import create_movie, delete_movie, get_movie_by_title, get_movies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    movies = get_movies()
    return templates.TemplateResponse(request, "index.html", {"movies": movies})


@router.get("/movies", response_class=HTMLResponse)
async def movie_list(request: Request):
    movies = get_movies()
    return templates.TemplateResponse(request, "movie_list.html", {"movies": movies})


@router.post("/movies", response_class=HTMLResponse)
async def create_new_movie(
    request: Request,
    title: str = Form(...),
    release_year: int = Form(...),
    genre: str = Form(...),
    director: str = Form(...),
    famous_actors: str = Form(...),
):
    famous_actors_list = famous_actors.split(",")
    movie_data = {
        "title": title,
        "release_year": release_year,
        "genre": genre,
        "director": director,
        "famous_actors": famous_actors_list,
    }
    movie = Movie(**movie_data)
    create_movie(movie)
    movies = get_movies()
    return templates.TemplateResponse(request, "movie_list.html", {"movies": movies})


@router.get("/movies/form", response_class=HTMLResponse)
async def movie_form(request: Request):
    return templates.TemplateResponse(request, "movie_form.html", {"request": request})


@router.get("/movies/{title}", response_class=HTMLResponse)
async def read_movie(request: Request, title: str):
    try:
        movie = get_movie_by_title(title)
        return templates.TemplateResponse(
            request, "movie_detail.html", {"movie": movie}
        )
    except HTTPException as e:
        return templates.TemplateResponse(
            request, "404.html", {"detail": e.detail}, status_code=404
        )


@router.delete("/movies/{title}", response_class=HTMLResponse)
async def delete_existing_movie(request: Request, title: str):
    delete_movie(title)
    movies = get_movies()
    return templates.TemplateResponse(request, "movie_list.html", {"movies": movies})
