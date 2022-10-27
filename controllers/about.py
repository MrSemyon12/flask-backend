from flask import render_template, request, session
from app import app


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
