import pandas as pd

SAMPLE_SIZE = 6
TOP_GENRES = 4
TOP_ACTORS = 32
TOP_DIRECTORS = 16


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


def get_top_genres_movies(conn, username: str):
    '''Фильмы самых популярных жанров пользователя из "смотреть позже".'''
    return pd.read_sql(f'''
        SELECT DISTINCT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
        WHERE genre_name IN (
            SELECT genre_name
                FROM (
                    SELECT genre_name, count(movie_id) as cnt
                    FROM
                        watch_later
                        JOIN movie_genre USING (movie_id)
                    WHERE username == :username
                    GROUP BY genre_name
                    ORDER BY cnt DESC
                    LIMIT {TOP_GENRES}
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
        LIMIT {SAMPLE_SIZE}
''', conn, params={'username': username})


def get_top_actors_movies(conn, username: str):
    '''Фильмы с участием самых популярных актеров пользователя.'''
    return pd.read_sql(f'''
        SELECT DISTINCT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
        WHERE movie_id IN (
            SELECT movie_id
            FROM
                movie
                JOIN movie_actor USING (movie_id)                
            WHERE actor_id IN (
                SELECT actor_id
                    FROM (
                        SELECT actor_id, count(movie_id) as cnt
                        FROM
                            watch_later
                            JOIN movie_actor USING (movie_id)
                        WHERE username == :username
                        GROUP BY actor_id
                        ORDER BY cnt DESC
                        LIMIT {TOP_ACTORS}
                    )
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
        LIMIT {SAMPLE_SIZE}
''', conn, params={'username': username})


def get_top_directors_movies(conn, username: str):
    '''Фильмы самых популярных режиссеров пользователя, исключая фильмы из "смотреть позже".'''
    return pd.read_sql(f'''
        SELECT DISTINCT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
        WHERE director_id IN (
            SELECT director_id
                FROM (
                    SELECT director_id, count(movie_id) as cnt
                    FROM
                        watch_later
                        JOIN movie USING (movie_id)
                    WHERE username == :username
                    GROUP BY director_id
                    ORDER BY cnt DESC
                    LIMIT {TOP_DIRECTORS}
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
        LIMIT {SAMPLE_SIZE}
''', conn, params={'username': username})
