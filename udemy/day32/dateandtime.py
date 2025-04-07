import json
import datetime as dt
name=input("enter the name: ")
d=input("enter the birthday: ")
email=input("enter the email: ")
file=open("bday.json","r")
origional=json.load(file)
file.close()
origional.update({name:{"bday":d,"email":email}})
file2=open("bday.json","w")
json.dump(origional,file2,indent=4)