"""
ex009 - DISTINCT Values

Task: Write a query that selects DISTINCT age values from `users`.
      (There are 3 users but only 2 unique ages.)

Schema: users(id INT, name TEXT, age INT)

Expected output:
  (25,)
  (30,)
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
for row in [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 22), (4, 'Dave', 30)]:
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", row)
conn.commit()

query = ""  # your SQL here

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
