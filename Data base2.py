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

olimp2 = ('Ломоносов', 'math', '1', '15.10.2021')
cur.execute("INSERT INTO olympia VALUES(?, ?, ?, ?);", olimp2)
conn.commit()

cur.execute("SELECT * FROM olympia;")
one_result = cur.fetchone()
print(one_result)
