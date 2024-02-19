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
    sql_query = ("SELECT cities.name FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    output = []
    for row in rows:
        for col in row:
            output.append(str(col))
    print(", ".join(output))
    connection.close()
