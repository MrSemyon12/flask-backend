from flask import render_template, request, session
from app import app


@app.route('/snake', methods=['GET'])
def snake():
    return render_template('snake.html')
