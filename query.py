import sqlite3

connection = sqlite3.connect("docSet.dsidx")

cursor = connection.cursor()
rows = cursor.execute(
    "SELECT * FROM searchIndex").fetchall()
print(rows)
