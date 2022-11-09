import pandas as pd


def get_movies(conn):
    return pd.read_sql('''
        SELECT *
        FROM movie
''', conn)


def get_movie(conn, movie_id):
    return pd.read_sql('''
        SELECT title, year, poster_url, group_concat(DISTINCT genre.name) AS genres
        FROM movie
        JOIN movie_genre
        JOIN genre
        WHERE movie.id == :id AND movie_id == movie.id AND genre_id == genre.id
        GROUP BY movie.id
''', conn, params={'id': movie_id})


def get_movie_director(conn, movie_id):
    return pd.read_sql('''
        SELECT director.name, photo_url
        FROM movie
        JOIN director
        WHERE movie.id == :id AND director.id == director_id
''', conn, params={'id': movie_id})


def get_movie_actors(conn, movie_id):
    return pd.read_sql('''
        SELECT actor.name, photo_url
        FROM movie
        JOIN movie_actor
        JOIN actor
        WHERE movie.id == :id AND movie.id == movie_id AND actor.id == actor_id
''', conn, params={'id': movie_id})


def get_reviews(conn, movie_id):
    return pd.read_sql('''
        SELECT user.name, post_date, comment, mark
        FROM movie
        JOIN review
        JOIN user
        WHERE movie.id == :id AND movie.id == movie_id AND user_id == user.id
''', conn, params={'id': movie_id})
