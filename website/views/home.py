from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from website import conn
from website.models.home import *

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
    return render_template('home_personal.html', user=current_user, len=len)
