"""
ex015 - IN Operator

Task: Write a query that selects all columns from `users`
      where `name` is IN ('Alice', 'Charlie').

Schema: users(id INT, name TEXT, age INT)

Expected output:
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

query = "SELECT * FROM users WHERE  name IN ('Alice','Charlie');"  # your SQL here

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
