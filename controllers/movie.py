from models.movie_model import get_film, get_film_director, get_film_actors, get_reviews
from flask import render_template
from app import app

from utils import get_db_connection

conn = get_db_connection()


@app.route('/movie/<int:id>', methods=['GET'])
def movie(id):
    return render_template(
        'movie.html',
        film=get_film(conn, id),
        director=get_film_director(conn, id),
        actors=get_film_actors(conn, id),
        reviews=get_reviews(conn, id),
        len=len
    )
