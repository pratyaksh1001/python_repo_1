import random
p=random.randrange(0,101)
c=input("choose the difficulty: ")
if c=='easy':
    x=10
elif c=='hard':
    x=5
v=0
r="you lost"
while v<=x:
    f=int(input("gurss the number: "))
    if p<f:
        print("too high")
        v+=1
    elif p>f:
        print("too low")
        v+=1
    else:
        r="you won"
        break
print(r)