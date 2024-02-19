#!/usr/bin/python3
'''
select and show the table content
'''


import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    state_name = sys.argv[4]
    connection = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
    cur = connection.cursor()
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    connection.close()
