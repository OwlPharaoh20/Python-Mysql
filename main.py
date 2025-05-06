from database import cursor, db 


def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user))
    db.commit()
    log.id = cursor.lastrowid
    print("Added log {}".format(log.id))