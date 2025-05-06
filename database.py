
#This file is like creating database . schema in MySQL
# In mongodb , this file is like creating user . schema in MongoDB
# Over here, you configure all data relating to the database owner & credentials  
import mysql.connector

config = {
    'user': 'root',
    'password': '1650.DutchMan',
    'host': '127.0.0.1',
    'database' : 'acme'
   
}

#Connect to database by creating a cursor and a database using the config
db = mysql.connector.connect(**config)
cursor = db.cursor(

)

