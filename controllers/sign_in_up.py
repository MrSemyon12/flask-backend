from models.sign_in_up_model import get_user, add_user
from flask import render_template, request, redirect
from app import app

from utils import get_db_connection

conn = get_db_connection()


@app.route('/sign-in', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user(conn, username)

        if len(user) and user.loc[0, 'password'] == password:
            return redirect('/movies')
        else:
            return render_template('sign_in.html', error=True)

    return render_template('sign_in.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(get_user(conn, username)):
            return render_template('sign_up.html', error=True)
        else:
            add_user(conn, username, password)
            return render_template('sign_in.html')

    return render_template('sign_up.html')
