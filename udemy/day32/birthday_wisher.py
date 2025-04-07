import smtplib
import datetime as dt
import json
passw="hjzo kwbq lujq jqxb"
my_email="pratyakshtest1@gmail.com"
file=open("bday.json", "r")
connection=smtplib.SMTP(host="smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email,password=passw)
data=json.load(file)
today=dt.datetime.today()
for i in data.keys():
    bday=data[i]["bday"].split(":")
    if int(bday[0])==today.day and int(bday[1])==today.month:
        connection.sendmail(from_addr="pratyakshtest1@gmail.com",to_addrs=data[i]["email"],msg=f"Subject:Happy Birthday {i}\n\nWishing you a very happy birthday {i}")