import pandas as pd


def get_film(conn, film_id):
    return pd.read_sql('''
        SELECT title, year, poster_url, rating, group_concat(DISTINCT genre_name) AS genres
        FROM film        
        JOIN film_genre USING (film_id)
        JOIN genre USING (genre_name)        
        WHERE film_id == :id
        GROUP BY film_id
''', conn, params={'id': film_id})


def get_film_director(conn, film_id):
    return pd.read_sql('''
        SELECT director_name, photo_url
        FROM film
        JOIN director USING (director_id)
        WHERE film_id == :id
''', conn, params={'id': film_id})


def get_film_actors(conn, film_id):
    return pd.read_sql('''
        SELECT actor_name, photo_url
        FROM film
        JOIN film_actor USING (film_id)
        JOIN actor USING (actor_id)
        WHERE film_id == :id
''', conn, params={'id': film_id})


def get_reviews(conn, film_id):
    return pd.read_sql('''
        SELECT user_name, post_date, comment, mark
        FROM film
        JOIN review USING (film_id)        
        WHERE film_id == :id
''', conn, params={'id': film_id})
