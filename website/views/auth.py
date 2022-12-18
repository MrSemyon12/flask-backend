from flask import Blueprint, render_template, url_for, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from website.models.user import User
from website import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Вы успешно вошли.', category='success')
            login_user(user, remember=True)
            return redirect(url_for('home.index'))
        else:
            flash('Не верные имя пользователя или пароль.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли.', category='success')
    return redirect(url_for('home.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if len(username) < 4:
            flash(
                'Имя пользователя должно содержать не менее 4-х символов.', category='error')
        elif len(password) < 4:
            flash('Пароль должен содержать не менее 4-х символов.', category='error')
        elif user:
            flash(f'Имя пользователя {username} занято.', category='error')
        else:
            new_user = User(
                username=username,
                password=generate_password_hash(password, method='sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегистрировались.', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('home.index'))

    return render_template('register.html', user=current_user)
