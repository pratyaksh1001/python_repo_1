import mysql.connector as sql
import numpy as np

mydb1=sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="pratyaksh1"
)
c1=mydb1.cursor()
c2=mydb1.cursor()

def check_routes():
    board=input("enter the boarding station: ")
    exit=input("enter the destination: ")
    c1.execute("select * from railway2")
    for i in c1:
        if (board.upper() in (i[2]).upper()) and (exit.upper() in (i[3]).upper()):
            print(i)

def check_by_tnum():
    num=int(input("enter the train number to view the data: "))
    c1.execute("select * from railway2" )
    for i in c1:
        if num==i[0]:
            print(i)
#check_routes()

def travel():
    start=input("enter the boarding station: ")
    end=input("enter the deboarding station: ")
    c1.execute("show tables")
    c2.execute("select * from railway2")
    for i in c1:
        c2.execute("select * from %s")
travel()
