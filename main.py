import sqlite3

conn = sqlite3.connect('kefir.db')
c = conn.cursor
c.execute('''select * from kefir''')
rows = c.fetchall()
print(rows)
conn.close()