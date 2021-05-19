import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="1234",
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE livros")


cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)