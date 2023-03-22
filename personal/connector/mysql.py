import mysql.connector as c
con=c.connect(host="localhost",user="root",password="123456789",database="store")
if con.connected():
    print("successfully connected")
else:
    print("error")