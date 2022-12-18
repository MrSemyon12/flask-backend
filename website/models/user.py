from website import db
from flask_login import UserMixin
import pandas as pd


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(255))


def get_top_genres(conn, username: str):
    '''Самые популярные жанры у пользователя.'''
    return pd.read_sql('''
        SELECT genre_name, count(movie_id) as cnt
        FROM
            movie
            JOIN watch_later USING (movie_id)
            JOIN movie_genre USING (movie_id)
        WHERE username == :username
        GROUP BY genre_name
        ORDER BY cnt DESC
    ''', conn, params={'username': username})


def get_top_actors(conn, username: str):
    '''Самые популярные актёры у пользователя.'''
    return pd.read_sql('''
        SELECT actor_name, count(movie_id) as cnt
        FROM
            movie
            JOIN watch_later USING (movie_id)
            JOIN movie_actor USING (movie_id)
            JOIN actor USING (actor_id)
        WHERE username == :username
        GROUP BY actor_name
        ORDER BY cnt DESC
    ''', conn, params={'username': username})
