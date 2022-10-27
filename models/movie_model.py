import pandas as pd


def get_film(conn, film_id):
    return pd.read_sql('''
        SELECT title, year, poster_url, rating, director_name, group_concat(DISTINCT genre_name), group_concat(DISTINCT actor_name)
        FROM film
        JOIN director USING (director_id)
        JOIN film_genre USING (film_id)
        JOIN genre USING (genre_name)  
        JOIN film_actor USING (film_id)
        JOIN actor USING (actor_id)
        WHERE film_id == :id
        GROUP BY film_id
''', conn, params={'id': film_id})
