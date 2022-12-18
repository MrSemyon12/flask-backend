from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_required
from website import conn
from website.models.movie import *

movie = Blueprint('movie', __name__)


@movie.route('/<int:movie_id>', methods=['GET'])
def info(movie_id):
    return render_template(
        'movie.html',
        movie=get_movie(conn, movie_id),
        watch_later=get_watch_later(
            conn, current_user.username) if current_user.is_authenticated else get_watch_later(conn, ''),
        mark=get_mark(
            conn, movie_id, current_user.username) if current_user.is_authenticated else get_mark(
            conn, movie_id, ''),
        actors=get_movie_actors(conn, movie_id),
        comments=get_comments(conn, movie_id),
        round=round,
        len=len
    )


@movie.route('/add_watch_later/<int:movie_id>', methods=['POST'])
@login_required
def add_watch_later(movie_id):
    add_to_watch_later(conn, (movie_id, current_user.username))
    return redirect(request.referrer)


@movie.route('/remove_watch_later/<int:movie_id>', methods=['POST'])
@login_required
def remove_watch_later(movie_id):
    remove_from_watch_later(conn, (movie_id, current_user.username))
    return redirect(request.referrer)


@movie.route('/comment/<int:movie_id>', methods=['POST'])
@login_required
def comment(movie_id):
    text = request.form.get('text')
    if text != '':
        add_comment(conn, (movie_id, current_user.username, text))
    return redirect(request.referrer)


@movie.route('/add_mark/<int:movie_id>/<int:mark>', methods=['POST'])
@login_required
def add_mark(movie_id, mark):
    add_new_mark(conn, (movie_id, current_user.username, mark))
    update_rating(conn, movie_id)
    return redirect(request.referrer)


@movie.route('/update_mark/<int:movie_id>/<int:mark>', methods=['POST'])
@login_required
def update_mark(movie_id, mark):
    update_old_mark(conn, (mark, movie_id, current_user.username))
    update_rating(conn, movie_id)
    return redirect(request.referrer)


@movie.route('/remove_mark/<int:movie_id>', methods=['POST'])
@login_required
def remove_mark(movie_id):
    remove_from_mark(conn, (movie_id, current_user.username))
    update_rating(conn, movie_id)
    return redirect(request.referrer)
