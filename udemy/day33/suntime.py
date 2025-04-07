import requests
import datetime as dt
my_lat=21.419537
my_longi=80.978821
para={"lat":21.419537,
        "lng":80.978821,
      "formatted":0}
Url="https://api.sunrise-sunset.org/json"
response=requests.get(url=Url,params=para)
data=response.json()["results"]
rise=data["sunrise"].split("T")[1].split("+")[0].split(":")
risetime=dt.time(int(rise[0]),int(rise[1]),int(rise[2]))
set=data["sunset"].split("T")[1].split("+")[0].split(":")
settime=dt.time(int(set[0]),int(set[1]),int(set[2]))