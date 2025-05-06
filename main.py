#In JS terms, this file is like the main.js, server.js, app.js
#This is like when you run your CRUD operations. Like create, read, update, delete data in the MYSQL database. 
#Also, it's like when you run your API endpoints in FastAPI
#

from database import cursor, db 



#Function to add logs to the database
def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


#create function to get logs
def get_logs():
    #write the sql query
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    #execute the sql query via the cursor
    cursor.execute(sql)
    result = cursor.fetchall()
    
    #print the result
    for row in result:
        print(row[1])



#create function to get a specific log
def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    
    for row in result:
        print(row)



def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log Updated")

    

def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log Deleted")


delete_log(5)
get_logs()



#update_log(2, 'Updated Log')
#get_logs()
#get_log(2)
#get_logs()







#add_log('This is log one', 'Brad')
#add_log('This is log two', 'John')
#add_log('This is log three', 'Jill')