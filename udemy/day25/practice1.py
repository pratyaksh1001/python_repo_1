import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
s=set(data["Shift"].to_list())
s=list(s)
print(s)
print(data[data["Hectare Squirrel Number"]==3]["Hectare Squirrel Number"].count())