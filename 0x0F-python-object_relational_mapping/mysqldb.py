#!/usr/bin/env python3
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root",
                  password="Million1234!", database="hbtn_0c_0")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS milla (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")
songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song3 (title) VALUES (%s)", (song,))
    print("Auto Increment ID: {}".format(cur.lastrowid))
db.commit()
print(cur.execute("SELECT * FROM song3 WHERE id = %s or id = %s", (13,14)))
numrows = cur.execute("SELECT * FROM song3")
print("Selected %s rows" % numrows)      
print("Selected %s rows" % cur.rowcount)

Print results in comma delimited format
any time you execute a database query you should surround it with a try/exception block.
try:
    cur.execute("SELECT * FROM song3")
    rows = cur.fetchall()
except MySQLdb.Error as e:
    try:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    except IndexError:
        print("MySQL Error: %s" % str(e))
for row in rows:
    for col in row:
        print("%s," %col, end=(""))
    print("\n")

cur.execute("SELECT * FROM song3 WHERE id = 13")
print("Id: %s -- Title: %s" % cur.fetchone())

# Close all cursors
cur.close()
# Close all databases
db.close()