# digits to word
n=input("enter the number: ")
d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
for i in n:
     x=int(i)
     print(d[x],end=" ")
print()