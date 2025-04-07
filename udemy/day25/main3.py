import pandas
d={
    "students":["hello","world","liyewfr"],
    "marks":[90,89,78]
}
data=pandas.DataFrame(d)
data.to_csv("generated.csv")
print(data)
# in this program i made a dataframe and used it to generate a csv file