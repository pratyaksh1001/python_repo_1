import csv
l=[]
with open("weather_data.csv") as data:
    d=csv.reader(data)
    for i in d:
        try:
            l.append(int(i[1]))
        except:
            continue

print(l)