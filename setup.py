#This file works like creating database . schema in MongoDB
#This file works like creating database . schema in MySQL
#This file works like creating database . schema in PostgreSQL
# also, here you configure all data relating to the MySQL database in the programming environment.



#import dependencies
import mysql.connector 
from mysql.connector import errorcode
from database import cursor


#create database variable 
DB_NAME = 'acme'


#Initialize tables, using a  dictionary data type 
TABLES = {}



#Create table dictionary titled logs
TABLES['logs'] = (
    "CREATE TABLE logs (" 
    #columns
    "id int(11) NOT NULL AUTO_INCREMENT,"
    "text varchar(250) NOT NULL,"
    "user varchar(250) NOT NULL,"
    "created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (id)"
    ") ENGINE=InnoDB" #table engine for 
)


# database creation function 
def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


# function to create tables 
def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    #create tables
    for table_name in TABLES:
        table_description = TABLES[table_name]
        #catch errors
        try:
           print("Creating table ({})".format(table_name), end="")
           cursor.execute(table_description)
        #if , return error 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists")
        #pass 
            else:
                print(err.msg)



create_database()
create_tables()