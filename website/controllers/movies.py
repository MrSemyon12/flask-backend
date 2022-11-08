from flask import Blueprint, render_template
from flask_login import current_user

movies = Blueprint('movies', __name__)


@movies.route('/', methods=['GET'])
def all():
    return render_template('movies.html', user=current_user)


@movies.route('/<int:id>', methods=['GET'])
def movie(id):
    return render_template(
        'movie.html',
        film=[],
        director=[],
        actors=[],
        reviews=[],
        len=len
    )
