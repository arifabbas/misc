import mysql.connector

mydb= mysql.connector.connect( host="localhost", username="root", password="root")
cursor=mydb.cursor();
cursor.execute("use db_practice")
# cursor.execute("create table student(name varchar(10), age int(3), class varchar(20))")
cursor.execute("show tables")

for x in cursor:
    print(x)
cursor.execute("desc student")

for x in cursor:
    print(x)

