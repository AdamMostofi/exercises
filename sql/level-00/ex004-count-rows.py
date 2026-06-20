"""
ex004 - COUNT Rows

Task: Write a SQL query that counts how many users are in the `users` table.
      The result column should be aliased as "total".

Schema:
  users(id INT, name TEXT, age INT)

Expected output:
  (3,)
"""

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
cur.execute("INSERT INTO users VALUES (1, 'Alice', 25)")
cur.execute("INSERT INTO users VALUES (2, 'Bob', 30)")
cur.execute("INSERT INTO users VALUES (3, 'Charlie', 22)")
conn.commit()

# Write your SQL query below (as a string):
query = "SELECT COUNT(*) FROM users"

# --- don't modify below ---
cur.execute(query)
for row in cur.fetchall():
    print(row)
conn.close()
