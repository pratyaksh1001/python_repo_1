import prettytable as pt

table=pt.PrettyTable()
table.add_column("name",["Pratyaksh","rahul","rohan","parul","priyal"])
table.add_column("roll",[1,2,3,4,5])
table.add_row(["hello",20])
table.align="l"
print(table)