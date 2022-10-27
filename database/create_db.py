import sqlite3
import pandas as pd

con = sqlite3.connect('database/filmoteka.sqlite')

f_damp = open('database/filmoteka.db', 'r', encoding='utf-8-sig')
damp = f_damp.read()
f_damp.close()

con.executescript(damp)
con.commit()

cursor = con.cursor()
df = pd.read_sql('''
    SELECT * FROM film
    JOIN director USING (director_id)
''', con)

print(df)

con.close()
