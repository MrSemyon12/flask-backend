import sqlite3


def get_db_connection():
    return sqlite3.connect('database/filmoteka.sqlite', check_same_thread=False)
