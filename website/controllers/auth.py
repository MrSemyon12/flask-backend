from flask import Blueprint, render_template, url_for, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from website.models import User
from website import db

auth = Blueprint('auth', __name__)


@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()

        if user and check_password_hash(user.password, password):
            flash('Вы успешно вошли.', category='success')
            login_user(user, remember=True)
            return redirect(url_for('movies.all'))
        else:
            flash('Не верные имя пользователя или пароль.', category='error')

    return render_template('sign_in.html', user=current_user)


@auth.route('/sign-out', methods=['GET', 'POST'])
@login_required
def sign_out():
    logout_user()
    flash('Вы успешно вышли.', category='success')
    return redirect(url_for('movies.all'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()

        if len(username) < 4:
            flash(
                'Имя пользователя должно содержать не менее 4-х символов.', category='error')
        elif len(password) < 4:
            flash('Пароль должен содержать не менее 4-х символов.', category='error')
        elif user:
            flash(f'Имя пользователя {username} занято.', category='error')
        else:
            new_user = User(
                name=username,
                password=generate_password_hash(password, method='sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегистрировались.', category='success')
            return redirect(url_for('auth.sign_in'))

    return render_template('sign_up.html', user=current_user)
