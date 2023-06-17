import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="mydb"
)

mycursor = mydb.cursor()

create_table = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
mycursor.execute(create_table)

mydb.commit()
mycursor.commit()
mycursor.close()
mydb.close()