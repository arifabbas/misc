import mysql.connector

print("Trying DB connection")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)
 
print(mysql)