import json

file=open("bday.json","w")
data={"Pratyaksh":{
    "bday":"11:09:2004",
    "email":"Pratyakshkarmahe@gmailo.com"
}}
json.dump(data,file,indent=4)