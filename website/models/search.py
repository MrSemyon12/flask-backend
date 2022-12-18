import pandas as pd


def find_pattern(conn, pattern: str):
    return pd.read_sql('''
        SELECT DISTINCT movie_id, title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM
            movie
            JOIN movie_genre USING (movie_id)
        WHERE movie_id IN (
            SELECT movie_id
            FROM
                movie
            WHERE low(title) LIKE low(:pattern)
            UNION
            SELECT movie_id
            FROM
                movie
                JOIN movie_genre USING (movie_id)
            WHERE low(genre_name) LIKE low(:pattern)
            UNION
            SELECT movie_id
            FROM
                movie
                JOIN director USING (director_id)
            WHERE low(director_name) LIKE low(:pattern)
            UNION
            SELECT movie_id
            FROM
                movie
                JOIN movie_actor USING (movie_id)
                JOIN actor USING (actor_id)
            WHERE low(actor_name) LIKE low(:pattern)
            UNION
            SELECT movie_id
            FROM
                movie
            WHERE low(country) LIKE low(:pattern)
            UNION
            SELECT movie_id
            FROM
                movie
            WHERE year LIKE low(:pattern)
        )
        GROUP BY movie_id
    ''', conn, params={'pattern': '%' + pattern + '%'})
