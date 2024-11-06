import mysql.connector

mysql_db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root"
)

cursor_db=mysql_db.cursor()
# cursor_db.execute("Create database db_practice")
cursor_db.execute("show databases")

print(cursor_db)
