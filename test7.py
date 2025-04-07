# josephus problem
l=eval(input("enter the list: "))
k=3
print(l)


def josephus(l,x,k):
     if len(l)==1:
          return l

     y=l[(x+k)%len(l)]
     l.remove(y)
     print(l)
     x=(x+k)%(len(l)+1)
     josephus(l,x,k)


res=josephus(l,0,k-1)