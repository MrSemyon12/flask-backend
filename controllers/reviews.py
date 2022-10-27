from models.reviews_model import get_reviews
from flask import render_template, request, session
from app import app

from utils import get_db_connection

conn = get_db_connection()


@app.route('/reviews', methods=['GET'])
def reviews():
    return render_template('reviews.html', reviews=get_reviews(conn), len=len)
