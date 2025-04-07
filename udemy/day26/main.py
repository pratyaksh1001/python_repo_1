import pandas
data=pandas.read_csv("../day25/50_states.csv")
for (i,j) in data.iterrows():
    print(j["state"])