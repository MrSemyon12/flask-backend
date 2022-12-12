from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from website import conn
from website.models.movies import *

movies = Blueprint('movies', __name__)


@movies.route('/', methods=['GET'])
def all():
    return render_template('movies.html', user=current_user, movies=get_movies(conn), len=len)


@movies.route('/<int:id>', methods=['GET', 'POST'])
def movie(id):
    if request.method == 'POST':
        text = request.form.get('comment')
        if (text != ''):
            comment = (id, current_user.user_name, text)
            add_comment(conn, comment)
        return redirect(url_for('movies.movie', id=id))

    return render_template(
        'movie.html',
        user=current_user,
        movie=get_movie(conn, id),
        director=get_movie_director(conn, id),
        actors=get_movie_actors(conn, id),
        comments=get_comments(conn, id),
        len=len
    )
