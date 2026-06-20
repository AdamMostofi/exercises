"""
ex006 - ORDER BY

Task: Write a query that selects all columns from `users`
      and orders the results by age from OLDEST to YOUNGEST.

Schema: users(id INT, name TEXT, age INT)

Expected output:
  (2, 'Bob', 30)
  (1, 'Alice', 25)
  (3, 'Charlie', 22)
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
for row in [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 22)]:
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", row)
conn.commit()

query = ""  # your SQL here

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
