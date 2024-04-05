import sqlite3

connection = sqlite3.connect("ACL2.docset/Contents/Resources/docSet.dsidx")

cursor = connection.cursor()

rows = cursor.execute(
    "SELECT count(*) FROM searchIndex ").fetchall()
print(rows)

rows = cursor.execute(
    "SELECT * FROM searchIndex WHERE name='Defun' LIMIT 10").fetchall()
print(rows)
