def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def dev(a,b):
    return a/b
d={
    '+':add,
    '-':sub,
    '*':mul,
    '/':dev
}
while True:
    x=input("enter the operator: ")

    if x in d.keys():
        a=int(input("enter the number: "))
        b=int(input("enter the number: "))
        print(a,x,b,"=",d[x](a,b),sep="")
    else:
        break
