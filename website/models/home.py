import pandas as pd

SAMPLE_SIZE = 6


def get_top_comments_movies(conn):
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
            JOIN genre USING (genre_name)
        GROUP BY movie_id
        ORDER BY cnt DESC, rating DESC
    ''', conn)


def get_top_last_time_movies(conn):
    return pd.read_sql(f'''
        SELECT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
            JOIN genre USING (genre_name)
        GROUP BY movie_id
        ORDER BY year DESC, rating DESC
        LIMIT {SAMPLE_SIZE}
    ''', conn)


def get_random_movies(conn):
    return pd.read_sql(f'''
        SELECT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
            JOIN genre USING (genre_name)
        GROUP BY movie_id
        ORDER BY RANDOM()
        LIMIT {SAMPLE_SIZE}
    ''', conn)
