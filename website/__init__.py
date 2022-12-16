from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sqlite3

db = SQLAlchemy()
basedir = path.abspath(path.dirname(__file__))
DB_NAME = 'db.sqlite3'
conn = sqlite3.connect(path.join(basedir, DB_NAME), check_same_thread=False)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sd2fa51ft3t5qfawaqq353d5wawe7&t&&iopp&997352ddafaaw92391--313145^^#@'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                            path.join(basedir, DB_NAME)
    db.init_app(app)

    from .views.auth import auth
    from .views.self import self
    from .views.games import games
    from .views.home import home
    from .views.movie import movie

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(self, url_prefix='/self')
    app.register_blueprint(games, url_prefix='/games')
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(movie, url_prefix='/movie')

    from .models.user import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
