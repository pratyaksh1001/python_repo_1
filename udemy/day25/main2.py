import pandas
data=pandas.read_csv("weather_data.csv")
x=data[data["day"]=="Monday"]
y=(x.temp*9/5)+32
print(y)