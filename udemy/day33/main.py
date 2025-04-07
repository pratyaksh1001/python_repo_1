import requests
import smtplib
import datetime as dt
import time
from suntime import my_longi,my_lat,risetime,settime
my_email=["vasugoyal3036@gmail.com","pratyakshkarmahe@gmail.com","shubham1293.be23@chitkara.edu.in"]    # ["pratyakshkarmahe@gmail.com","pratyaksh0856.be23@chitkara.edu.in"]
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user="pratyakshtest1@gmail.com",password="hjzo kwbq lujq jqxb")
while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longi=float(data["iss_position"]["longitude"])
    latit=float(data["iss_position"]["latitude"])
    now=dt.datetime.now()
    for ems in my_email:
        connection.sendmail(from_addr="pratyakshtest1@gmail.com",to_addrs=ems,msg=f"Subject:The ISS is about to appear !! \n\nThe current position of ISS is:\n{latit} latitude\n{longi} longitude\nwhere your position is: \n{my_lat} latitude\n{my_longi} longitude")
        print(f"Subject:The ISS is about to appear !! \n\nThe current position of ISS is:\n{latit} latitude\n{longi} longitude\n\nwhere your position is: \n{my_lat} latitude\n{my_longi} longitude\n\nthe distance from ISS is:\n{latit-my_lat} latitude\n{longi-my_longi} longitude\n\n\n\n")
    #time.sleep(30)