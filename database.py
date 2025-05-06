import mysql.connector

config = {
    'user': 'root',
    'password': '1650.DutchMan',
    'host': '127.0.0.1',
    'database' : 'acme'
   
}

db = mysql.connector.connect(**config)
cursor = db.cursor(
    
)