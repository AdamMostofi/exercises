"""
ex005 - Select Specific Columns

Task: Write a query that selects only `name` and `age` columns
      from the `users` table (not `id`).

Schema: users(id INT, name TEXT, age INT)

Expected output:
  ('Alice', 25)
  ('Bob', 30)
  ('Charlie', 22)
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
for row in [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 22)]:
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", row)
conn.commit()

query = "SELECT name, age FROM users;"  # your SQL here

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
