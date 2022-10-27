import pandas as pd


def get_reviews(conn):
    return pd.read_sql('''
        SELECT * FROM review
''', conn)
