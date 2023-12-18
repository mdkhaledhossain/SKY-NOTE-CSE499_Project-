import mysql.connector

conn = mysql.connector.connect(host='localhost',username='root',password='',database='skynotedb')
my_cursor=conn.cursor()

conn.commit()
conn.close

# print("Connection Succesfully created!!!")