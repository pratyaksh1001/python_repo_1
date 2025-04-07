import smtplib
import datetime as dt
import random
import calendar
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
mails=["parul0848.be23@chitkara.edu.in","prabhleen0851.be23@chitkara.edu.in","priyal0857.be23@chitkara.edu.in","pratyakshkarmahe@gmail.com","muskansinghdps9@gmail.com"]
file=open("quotes.txt","r")
quotes=file.readlines()

for email in mails:
    now = dt.datetime.now()
    q = random.choice(quotes).split("-")
    d = f"{dt.datetime.now().day}:{dt.datetime.now().month}:{dt.datetime.now().year} {calendar.day_name[dt.datetime.today().weekday()]}"
    connection.login(user="pratyakshtest1@gmail.com",password="hjzo kwbq lujq jqxb")
    connection.sendmail(from_addr="pratykshtest1@gmail.com",to_addrs=email,msg=f"Subject:Spamming you with mails\n\n {d}'s quote is: \n {q[0]}\nby - {q[1]}")
