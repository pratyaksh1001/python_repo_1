# write a program which prints all the divisors of a number
n=int(input("enter the number: "))
f=0;
for i in range(2,n):
     if n%i==0:
          f+=1
          print(i," is a divisor of ",n)