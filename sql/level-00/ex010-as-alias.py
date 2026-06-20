"""
ex010 - AS Alias

Task: Write a query that selects `name` and `age` from `users`,
      but renames the `age` column to `years_old` using AS.

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

query = ""  # your SQL here (use AS to alias age)

cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
