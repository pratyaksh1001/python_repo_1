# binary search
l=eval(input("enter the list: "))
l.sort()
print(l)
def binsearch(lst,k,low,high):
    s=len(l)
    mid=(low+high)//2
    for i in range(0,s):
        if l[mid]==k:
            return mid
        elif l[mid]>k:
            binsearch(lst,k,low,mid-1)
        elif l[mid]<k:
            binsearch(lst,k,mid+1,high)
x=int(input("enter the key: "))
print("the index is: ",binsearch(l,x,0,len(l)))