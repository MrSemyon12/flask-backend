import pandas as pd


def get_actor(conn, actor_id):
    return pd.read_sql('''
        SELECT *
        FROM 
            actor
        WHERE actor_id == :id        
''', conn, params={'id': actor_id})
