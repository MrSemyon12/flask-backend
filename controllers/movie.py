from models.movie_model import get_film
from flask import render_template, request, session
from app import app

from utils import get_db_connection

conn = get_db_connection()


@app.route('/movie/<int:id>', methods=['GET'])
def movie(id):
    return render_template('movie.html', film=get_film(conn, id), len=len)
