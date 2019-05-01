import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='prithi08',
                             db='schooldb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

try:

    with connection.cursor() as cursor:

        # SQL
        sql = "SELECT * from student "

        # Execute query.
        cursor.execute(sql)

        #print("cursor.description: ", cursor.description)

        #print()

        for row in cursor:
            for key, value in row.items():
                pass

finally:
    # Close connection.
    connection.close()
