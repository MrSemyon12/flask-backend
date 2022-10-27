import pandas as pd


def get_films(conn):
    return pd.read_sql('''
        SELECT film_id, title, year, director_name, rating, poster_url
        FROM film
        JOIN director USING (director_id)
''', conn)
