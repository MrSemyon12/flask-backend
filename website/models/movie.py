import pandas as pd

SAMPLE_SIZE = 6


def get_movie(conn, movie_id):
    return pd.read_sql('''
        SELECT movie_id, title, year, poster_url, director_name, group_concat(DISTINCT genre_name) AS genres, rating
        FROM
            movie
            JOIN director USING (director_id)
            JOIN movie_genre USING (movie_id)
            JOIN genre USING (genre_name)
        WHERE movie_id == :id
        GROUP BY movie_id
    ''', conn, params={'id': movie_id})


def get_movie_director(conn, movie_id):
    return pd.read_sql('''
        SELECT *
        FROM 
            movie
            JOIN director USING (director_id)
        WHERE movie_id == :id
    ''', conn, params={'id': movie_id})


def get_movie_actors(conn, movie_id):
    return pd.read_sql('''
        SELECT *
        FROM
            movie
            JOIN movie_actor USING (movie_id)
            JOIN actor USING (actor_id)
        WHERE movie_id == :id
    ''', conn, params={'id': movie_id})


def get_comments(conn, movie_id):
    return pd.read_sql('''
        SELECT username, post_date, text
        FROM
            movie
            JOIN comment USING (movie_id)
            JOIN user USING (username)
        WHERE movie_id == :id
    ''', conn, params={'id': movie_id})


def add_comment(conn, comment):
    cursor = conn.cursor()
    sql = 'INSERT INTO comment (movie_id, username, text) VALUES (?, ?, ?)'
    cursor.execute(sql, comment)
    # sql = 'UPDATE movie SET rating = (SELECT AVG(mark) FROM review WHERE movie_id = ?) WHERE movie_id = ?'
    # cursor.execute(sql, (review[0], review[0]))
    conn.commit()


def add_to_watch_later(conn, record):
    cursor = conn.cursor()
    sql = 'INSERT INTO watch_later (movie_id, username) VALUES (?, ?)'
    cursor.execute(sql, record)
    conn.commit()


def get_watch_later(conn, username):
    return pd.read_sql('''
        SELECT movie_id
        FROM
            watch_later
        WHERE username == :username
    ''', conn, params={'username': username})
