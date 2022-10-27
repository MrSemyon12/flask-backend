from models.movies_model import get_films
from flask import render_template, request, session
from app import app

from utils import get_db_connection

conn = get_db_connection()


@app.route('/movies', methods=['GET'])
def movies():
    return render_template('movies.html', films=get_films(conn), len=len)
