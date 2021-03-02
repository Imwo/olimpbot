import sqlite3

import datetime

con = sqlite3.connect('olimpiads.db')

cur = con.cursor()

cur.execute('create table if not exists list_olimps (name text, subject text, level integer, date date)')


con.commit()
cur.execute("SELECT * FROM list_olimps")
print (cur.fetchall())

cur.execute('create table if not exists users(user_id integer not null, user_name text, user_surname text, class integer)')

con.commit()

