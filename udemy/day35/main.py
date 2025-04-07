import requests
import json
import datetime as dt
weather_key="2a0fcdd997736e5a4eda82776b95dc77"
api_url="https://api.openweathermap.org/data/2.5/forecast"
parameters={"lat":21.417700,"lon":80.979600,"appid":weather_key,"cnt":4}
connection=requests.get(url=api_url,params=parameters)
data=connection.json()
file=open("weather_data.json","w")
json.dump(data,file,indent=4)
data=data["list"]
max_temp=0
min_temp=1000
rain=[]
for i in data:
    i["main"]["temp"]-=274
    i["main"]["feels_like"]-=274
    i["main"]["temp_max"]-=274
    i["main"]["temp_min"]-=274
    if i["main"]["temp"]>max_temp:
        max_temp=i["main"]["temp"]
    if i["main"]["temp"]<min_temp:
        min_temp=i["main"]["temp"]

for i in data:
    print(f"Weather at time : {i["dt_txt"]} is - \n")
    for j in i["main"].keys():
        print(f"{j} - {i["main"][j]}")
    print(f"weather - {i["weather"][0]["main"]}")
    if i["weather"][0]["main"]=="Rain":
        rain.append(i["dt_txt"])
    print("\n")
print(f"The max temperature of the days is: {max_temp}")
print(f"The min temperature of the days is: {min_temp}")
print("The possible dates and time of rain are -")
final=[]
for i in rain:
    x=i.split(" ")
    date=x[0].split("-")
    time=x[1].split(":")
    y=dt.datetime(year=int(date[0]),month=int(date[1]),day=int(date[2]),hour=int(time[0]),minute=int(time[1]))
    final.append(y)
    print(y)