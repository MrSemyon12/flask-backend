from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from website import conn
from website.models.movies import *

home = Blueprint('home', __name__)


@home.route('/general', methods=['GET'])
def home_general():
    return render_template('home_general.html', user=current_user, movies=get_movies(conn), len=len)


@home.route('/personal', methods=['GET'])
@login_required
def home_personal():
    return render_template('home_personal.html', user=current_user, len=len)


@home.route('/<int:movie_id>', methods=['POST'])
@login_required
def add_to_watch_later(movie_id):
    add_watch_later(conn, (movie_id, current_user.username))
    return redirect(url_for('home.home_personal'))


@home.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
def movie(movie_id):
    if request.method == 'POST':
        text = request.form.get('comment')
        if text != '':
            comment = (movie_id, current_user.username, text)
            add_comment(conn, comment)
        return redirect(url_for('home.movie', movie_id=movie_id))

    return render_template(
        'movie.html',
        user=current_user,
        movie=get_movie(conn, movie_id),
        director=get_movie_director(conn, movie_id),
        actors=get_movie_actors(conn, movie_id),
        comments=get_comments(conn, movie_id),
        len=len
    )
