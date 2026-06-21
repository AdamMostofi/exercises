"""
ex014 - BETWEEN

Task: Write a query that selects all columns from `users`
      where `age` is BETWEEN 23 and 30 (inclusive).

Schema: users(id INT, name TEXT, age INT)

Expected output:
  (1, 'Alice', 25)
  (2, 'Bob', 30)
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
for row in [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 22)]:
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", row)
conn.commit()

query = "SELECT * FROM users WHERE  age BETWEEN 23 AND 30 ;"  # your SQL here

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
