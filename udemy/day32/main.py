import smtplib
import datetime as dt
import random
import calendar
file=open("quotes.txt","r")
quotes=file.readlines()
my_email="pratyakshtest1@gmail.com"
passw="hjzo kwbq lujq jqxb"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(password=passw,user=my_email)
now=dt.datetime.now()
q=random.choice(quotes).split("-")
d=f"{dt.datetime.now().day}:{dt.datetime.now().month}:{dt.datetime.now().year} {calendar.day_name[dt.datetime.today().weekday()]}"
connection.sendmail(from_addr=my_email,to_addrs="pratyakshkarmahe@gmail.com",msg=f"Subject:The Pratyaksh's mail service\n\n {d}'s quote is: \n {q[0]}\nby - {q[1]}")
print(f"Subject:The Pratyaksh's mail service\n\n {d}'s quote is: \n {q[0]}\nby - {q[1]}")