s=input("enter the message: ")

x=4
def func1(x,s):
    s2=""
    for i in s:
        if i.isalpha():
            if ord(i)+x>=ord('z'):
                s2+=chr(ord(i)-52+x)
            else:
                s2+=chr(ord(i)+x)
        else:
            s2+=i
    return s2
y=func1(x,s)
def func2(x,y):
    s2=""
    for i in s:
        if i.isalpha():
            if ord(i)-x<='A':
                s2+=chr(ord(i)+52-x)
            else:
                s2+=i
        else:
            s2+=i
    return s2
print(func2(x,y))