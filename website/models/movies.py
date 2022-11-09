import pandas as pd


def get_movies(conn):
    return pd.read_sql('''
        SELECT movie_id, title, year, director_name, group_concat(DISTINCT genre_name) AS genres
        FROM 
            movie
            JOIN director USING (director_id)
            JOIN movie_genre USING (movie_id)
            JOIN genre USING (genre_name)
        GROUP BY movie_id
''', conn)


def get_movie(conn, movie_id):
    return pd.read_sql('''
        SELECT title, year, poster_url, group_concat(DISTINCT genre_name) AS genres
        FROM 
            movie            
            JOIN movie_genre USING (movie_id)
            JOIN genre USING (genre_name)
        WHERE movie_id == :id
        GROUP BY movie_id
''', conn, params={'id': movie_id})


def get_movie_director(conn, movie_id):
    return pd.read_sql('''
        SELECT director_name, photo_url
        FROM movie
        JOIN director USING (director_id)
        WHERE movie_id == :id
''', conn, params={'id': movie_id})


def get_movie_actors(conn, movie_id):
    return pd.read_sql('''
        SELECT actor_name, photo_url
        FROM
            movie
            JOIN movie_actor USING (movie_id)
            JOIN actor USING (actor_id)
        WHERE movie_id == :id
''', conn, params={'id': movie_id})


def get_reviews(conn, movie_id):
    return pd.read_sql('''
        SELECT user_name, post_date, comment, mark
        FROM 
            movie
            JOIN review USING (movie_id)
            JOIN user USING (user_name)
        WHERE movie_id == :id
''', conn, params={'id': movie_id})
