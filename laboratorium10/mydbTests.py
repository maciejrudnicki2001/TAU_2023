import mysql.connector
import unittest

class TestMydb(unittest.TestCase):
    def setUp(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="user",
            passwd="password",
            database="mydb"
        )
        self.mycursor = self.mydb.cursor()
        self.create_table = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
        self.mycursor.execute(self.create_table)
        self.mydb.commit()

    def tearDown(self):
        self.mycursor.close()
        self.mydb.close()

    def test_create_user_table(self):

        add_user_sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        user_data = ("John", "Highway 21")
        self.mycursor.execute(add_user_sql, user_data)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        self.assertEqual(myresult[0], ('John', 'Highway 21'))

    def test_read_user_table(self):
        add_user_sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        user_data = ("John", "Highway 21")
        self.mycursor.execute(add_user_sql, user_data)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        self.assertEqual(myresult[0], ('John', 'Highway 21'))
    
    def test_update_user_table(self):
        add_user_sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        user_data = ("John", "Highway 21")
        self.mycursor.execute(add_user_sql, user_data)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        self.assertEqual(myresult[0], ('John', 'Highway 21'))

        update_user_sql = "UPDATE customers SET address = %s WHERE name = %s"
        update_data = ("Valley 345", "John")
        self.mycursor.execute(update_user_sql, update_data)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        self.assertEqual(myresult[0], ('John', 'Valley 345'))
    
    def test_delete_user_table(self):
        add_user_sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        user_data = ("John", "Highway 21")
        self.mycursor.execute(add_user_sql, user_data)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        self.assertEqual(myresult[0], ('John', 'Highway 21'))

        delete_user_sql = "DELETE FROM customers WHERE name = %s"
        delete_data = ("John", )
        self.mycursor.execute(delete_user_sql, delete_data)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        self.assertEqual(myresult, [])

if __name__ == '__main__':
    unittest.main()