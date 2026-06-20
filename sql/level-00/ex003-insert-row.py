"""
ex003 - INSERT a Row

Task: Write a SQL query that inserts a new user into the `users` table:
      id=4, name='Diana', age=28.
      Then SELECT * FROM users to verify.

Schema:
  users(id INT, name TEXT, age INT)

Expected output (after your INSERT + SELECT):
  (1, 'Alice', 25)
  (2, 'Bob', 30)
  (3, 'Charlie', 22)
  (4, 'Diana', 28)
"""

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT, age INT)")
cur.execute("INSERT INTO users VALUES (1, 'Alice', 25)")
cur.execute("INSERT INTO users VALUES (2, 'Bob', 30)")
cur.execute("INSERT INTO users VALUES (3, 'Charlie', 22)")
conn.commit()

# Write your INSERT query below (as a string):
insert_query = "INSERT INTO users (id,name,age) VALUES (4, 'Diana', 28)"

# Write your SELECT query below (to verify):
select_query = "SELECT * FROM users"

# --- don't modify below ---
cur.execute(insert_query)
conn.commit()
cur.execute(select_query)
for row in cur.fetchall():
    print(row)
conn.close()
