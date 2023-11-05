import sqlite3
PATH = "database/profile_information.db"
cx = sqlite3.connect(PATH)
cu = cx.cursor()

# query = cu.execute('SELECT * FROM Users')
# print(query.fetchall())

def get_id_from_email(email):
    sql = 'SELECT employee_id FROM Users WHERE email_address = "%s"' % email
    query = cu.execute(sql)
    id = query.fetchone()
    if(id):
        return id[0]
    else:
        return False

#print(emailExistsInUsers(("danaetroupe@gmail.com")))
#print(emailExistsInUsers(('lalala')))

cx.close()