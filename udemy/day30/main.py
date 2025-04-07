import json

file=open("test.json","r")
#d1={"Pratyaksh Karmahe":{"score":100,"roll":11}}
#d1.update({"rahul":{"score":10,"roll":12}})
print(json.load(file))