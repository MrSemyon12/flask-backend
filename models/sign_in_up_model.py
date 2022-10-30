import pandas as pd


def get_user(conn, username):
    return pd.read_sql('''
        SELECT *
        FROM user
        WHERE user_name == :name
''', conn, params={'name': username})


def add_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(f'''
    INSERT INTO user (user_name, password) VALUES
    ('{username}', '{password}');
    ''')
    conn.commit()
