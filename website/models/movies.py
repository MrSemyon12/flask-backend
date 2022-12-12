import pandas as pd


def get_movies(conn):
    return pd.read_sql('''
        SELECT movie_id, title, year, director_name, group_concat(DISTINCT genre_name) AS genres
        FROM
            movies
            JOIN directors USING (director_id)
            JOIN movie_genres USING (movie_id)
            JOIN genres USING (genre_name)
        GROUP BY movie_id
''', conn)


def get_movie(conn, movie_id):
    return pd.read_sql('''
        SELECT movie_id, title, year, poster_url, group_concat(DISTINCT genre_name) AS genres, rating
        FROM
            movies
            JOIN movie_genres USING (movie_id)
            JOIN genres USING (genre_name)
        WHERE movie_id == :id
        GROUP BY movie_id
''', conn, params={'id': movie_id})


def get_movie_director(conn, movie_id):
    return pd.read_sql('''
        SELECT *
        FROM 
            movies
            JOIN directors USING (director_id)
        WHERE movie_id == :id
''', conn, params={'id': movie_id})


def get_movie_actors(conn, movie_id):
    return pd.read_sql('''
        SELECT *
        FROM
            movies
            JOIN movie_actors USING (movie_id)
            JOIN actors USING (actor_id)
        WHERE movie_id == :id
''', conn, params={'id': movie_id})


def get_comments(conn, movie_id):
    return pd.read_sql('''
        SELECT user_name, post_date, text
        FROM
            movies
            JOIN comments USING (movie_id)
            JOIN user USING (user_name)
        WHERE movie_id == :id
''', conn, params={'id': movie_id})


def add_comment(conn, comment):
    cursor = conn.cursor()
    sql = 'INSERT INTO comments (movie_id, user_name, text) VALUES (?, ?, ?)'
    cursor.execute(sql, comment)
    # sql = 'UPDATE movie SET rating = (SELECT AVG(mark) FROM review WHERE movie_id = ?) WHERE movie_id = ?'
    # cursor.execute(sql, (review[0], review[0]))
    conn.commit()
