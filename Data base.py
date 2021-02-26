import sqlite3

conn = sqlite3.connect('olimpiads.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS olympia(
   olympname TEXT,
   subject TEXT,
   level INT
   time INT);
""")
conn.commit()

cur.execute("""INSERT INTO olympia(olympname, subject, level, time) 
   VALUES('Высшая проба', 'math', '1', '29.10.2021');""")
conn.commit()

olimp2 = ('')
