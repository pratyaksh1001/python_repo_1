import random
d = {
    "name1":1000,"name2":50000,"name3":200,"name4":500,"name5":4000
}
score=0
f1=random.choice(list(d.keys()))
def func1(s,f1):
    f2=random.choice(list(d.keys()))
    while f1==f2:
        f2=random.choice(list(d.keys()))
    print(f1,":",d[f1])
    print(f2)
    x=input("enter higher or lower: ")
    if x=='higher':
        if d[f1]<d[f2]:
            print("the guess is right")
            s+=1
            func1(s,f2)
        else:
            print("the guess was wrong")
            print("score is:",s)
            return s
    elif x=='lower':
        if d[f1]>d[f2]:
            print("the guess is right")
            s+=1
            func1(s,f2)
        else:
            print("the guess was wrong")
            print("score is:",s)
            return s

func1(score,f1)