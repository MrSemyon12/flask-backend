from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from website import conn
from website.models.movies import *

movies = Blueprint('movies', __name__)


@movies.route('/', methods=['GET'])
def all_movies():
    return render_template('movies.html', user=current_user, movies=get_movies(conn), len=len)


@movies.route('/<int:movie_id>', methods=['GET', 'POST'])
def movie_by_id(movie_id):
    if request.method == 'POST':
        text = request.form.get('comment')
        if text != '':
            comment = (movie_id, current_user.user_name, text)
            add_comment(conn, comment)
        return redirect(url_for('movies.movie_by_id', movie_id=movie_id))

    return render_template(
        'movie.html',
        user=current_user,
        movie=get_movie(conn, movie_id),
        director=get_movie_director(conn, movie_id),
        actors=get_movie_actors(conn, movie_id),
        comments=get_comments(conn, movie_id),
        len=len
    )
