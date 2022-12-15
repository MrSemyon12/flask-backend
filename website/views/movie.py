from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from website import conn
from website.models.movie import *

movie = Blueprint('movie', __name__)


@movie.route('/<int:movie_id>', methods=['GET'])
def info(movie_id):
    return render_template(
        'movie.html',
        user=current_user,
        movie=get_movie(conn, movie_id),
        director=get_movie_director(conn, movie_id),
        actors=get_movie_actors(conn, movie_id),
        comments=get_comments(conn, movie_id),
        len=len
    )


@movie.route('/watch_later/<int:movie_id>', methods=['POST'])
@login_required
def watch_later(movie_id):
    add_to_watch_later(conn, (movie_id, current_user.username))
    return redirect(request.referrer)


@movie.route('/comment/<int:movie_id>', methods=['POST'])
@login_required
def comment(movie_id):
    text = request.form.get('text')
    if text != '':
        add_comment(conn, (movie_id, current_user.username, text))
    return redirect(request.referrer)
