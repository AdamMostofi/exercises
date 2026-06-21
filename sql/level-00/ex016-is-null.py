"""
ex016 - IS NULL

Task: Write a query that selects all columns from `users`
      where `email` IS NULL.

Schema: users(id INT, name TEXT, email TEXT)

Expected output:
  (2, 'Bob', None)
  (3, 'Charlie', None)
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, email TEXT)")
for row in [(1, 'Alice', 'alice@mail.com'), (2, 'Bob', None), (3, 'Charlie', None)]:
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", row)
conn.commit()

query = ""  # your SQL here (use IS NULL, not = NULL)

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
