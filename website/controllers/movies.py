from flask import Blueprint, render_template
from flask_login import current_user
from website import conn
from website.models.movies import *

movies = Blueprint('movies', __name__)


@movies.route('/', methods=['GET'])
def all():
    return render_template('movies.html', user=current_user, movies=get_movies(conn), len=len)


@movies.route('/<int:id>', methods=['GET', 'POST'])
def movie(id):
    return render_template(
        'movie.html',
        user=current_user,
        movie=get_movie(conn, id),
        director=get_movie_director(conn, id),
        actors=get_movie_actors(conn, id),
        reviews=get_reviews(conn, id),
        len=len
    )
