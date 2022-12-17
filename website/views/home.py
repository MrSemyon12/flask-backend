from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from website import conn
from website.models.home import *
from website.models.movie import get_watch_later

home = Blueprint('home', __name__)


@home.route('/general', methods=['GET'])
def general():
    return render_template(
        'home_general.html',
        user=current_user,
        top_comments_movies=get_top_comments_movies(conn),
        top_last_time_movies=get_top_last_time_movies(conn),
        random_movies=get_random_movies(conn),
        len=len
    )


@home.route('/personal', methods=['GET'])
@login_required
def personal():
    return render_template(
        'home_personal.html',
        user=current_user,
        top_genres_movies=get_top_genres_movies(conn, current_user.username),
        # top_actors_movies=get_top_actors_movies(conn, current_user.username),
        # top_directors_movies=get_top_directors_movies(
        #     conn, current_user.username),
        watch_later=get_watch_later(conn, current_user.username),
        len=len
    )
