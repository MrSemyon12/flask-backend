from website import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(255))


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    photo_url = db.Column(db.String(255))


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    photo_url = db.Column(db.String(255))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    year = db.Column(db.Integer)
    poster_url = db.Column(db.String(255))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))


class Movie_actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))


class Movie_genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_date = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    mark = db.Column(db.Integer)
