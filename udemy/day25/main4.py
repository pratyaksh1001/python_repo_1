import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
d={
    "Primary Fur Color":["Black","Gray","Cinnamon"],
    "count":[0,0,0]
}
for i in range(len(d["count"])):
    d["count"][i]=data[data["Primary Fur Color"]==d["Primary Fur Color"][i]]["Primary Fur Color"].count()
data2=pandas.DataFrame(d)
print(data2)
data2.to_csv("squrrel_generated.csv")