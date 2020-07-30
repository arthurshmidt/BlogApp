from random import randint
import mariadb
import datetime
import time

# general syntax for connecting to MariaDB server
# mysql -u root -p
# USE to connect
# SHOW to display
# SELECT FROM to read
# DROP to delete

class database:
    def __init__(self):
        self.table = None
        self.conn = None
        self.C = None

    def connect(self):
        self.conn = mariadb.connect(
            user="root",
            password="password",
            host="localhost",
            database="blog_posts"
            )
        self.C = self.conn.cursor()

    def addTable(self,date_input):
        """

        Basic table layout: (name of table) = date -> summary, post, unique ID

        """
        d = datetime.datetime.now()
        new_table = "CREATE TABLE " + date_input + " (Summary LONGTEXT, Post LONGTEXT, data_id INTEGER AUTO_INCREMENT PRIMARY KEY)"
        self.C.execute(new_table)

    def addData(self,table_name,summary_data,post_data):
        sql_entry_data = "INSERT INTO " + table_name + " (Summary, Post) VALUES (%s, %s)"
        val = (summary_data,post_data)
        self.C.execute(sql_entry_data, val)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()

    # returns an array of table names
    def returnTables(self):
        self.C.execute("SHOW TABLES")
        myresult = self.C.fetchall()
        tables_list = []
        for x in myresult:
            tables_list.append(x[0])

        return tables_list

    # returns the contents (tuple) of a table 
    def returnTableValues(self):
        continue

if __name__ == "__main__":
    # testing of the database class

    # test connection to database and the instertion of a post
    data = database()
    data.connect()
    data.addTable("D2020_07_28")
    summary_post = "This summary post is test my sql database entry and retrieval"
    body_post = "This text is meant to represent the body of the blog post.  Yay!!!!!.  Better than Lorem Ipsum -> These are the voyages of the starship Enterprise. Its five-year mission: to explore strange new worlds, to seek out new life and new civilizations, to boldly go where no man has gone before"
    data.addData("D2020_07_23", summary_post, body_post)
    print("Entered Data into sql")

    # retrieve and display blog posts from sql
    tables_list = data.returnTables()
    print(tables_list)

    # close out the connection to database
    data.disconnect()
