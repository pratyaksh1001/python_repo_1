import mysql.connector as con

connection = con.connect(host='localhost',password="1234",user='root',database='db1')

cursor=connection.cursor()



for i in l:
    cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",i)
connection.commit()