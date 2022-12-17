import pandas as pd

SAMPLE_SIZE = 6


def get_top_comments_movies(conn):
    '''Фильмы с наибольшим количеством комментариев.'''
    return pd.read_sql(f'''
        SELECT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            (
                SELECT movie_id, title, year, poster_url, rating, count(text) as cnt
                FROM
                    movie
                    LEFT JOIN comment USING (movie_id)
                GROUP BY movie_id
                ORDER BY cnt DESC, rating DESC      
                LIMIT {SAMPLE_SIZE}
            )
            JOIN movie_genre USING (movie_id)            
        GROUP BY movie_id
        ORDER BY cnt DESC, rating DESC
    ''', conn)


def get_top_last_time_movies(conn):
    '''Фильмы с самым высоким рейтингом, сортировка по году.'''
    return pd.read_sql(f'''
        SELECT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)            
        GROUP BY movie_id
        ORDER BY year DESC, rating DESC
        LIMIT {SAMPLE_SIZE}
    ''', conn)


def get_random_movies(conn):
    '''Набор случайных фильмов.'''
    return pd.read_sql(f'''
        SELECT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)            
        GROUP BY movie_id
        ORDER BY RANDOM()
        LIMIT {SAMPLE_SIZE}
    ''', conn)


def get_top_genres_movies(conn, username):
    '''Фильмы трех самых популярных жанров пользователя из "смотреть позже", исключая фильмы из "смотреть позже".'''
    return pd.read_sql('''
        SELECT DISTINCT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
        WHERE genre_name IN (
            SELECT genre_name
                FROM (
                    SELECT genre_name, count(movie_id) as cnt
                    FROM
                        movie
                        JOIN watch_later USING (movie_id)
                        JOIN movie_genre USING (movie_id)
                    WHERE username == :username
                    GROUP BY genre_name
                    ORDER BY cnt DESC
                    LIMIT 3
                )
        )
        AND movie_id NOT IN (
            SELECT movie_id
            FROM
                watch_later
            WHERE username == :username
        )
        GROUP BY movie_id
        ORDER BY RANDOM()
        LIMIT 6
''', conn, params={'username': username})


def get_top_actors_movies(conn, username):
    '''Фильмы с участием десяти самых популярных актеров пользователя в случаном порядке.'''
    pass


def get_top_directors_movies(conn, username):
    '''Фильмы пяти самых популярных режиссеров пользователя, исключая фильмы из "смотреть позже".'''
    pass
