# write a code to find the maximum possible profit and loss
l=[7,3,5,-8,1,4,-9]
m=0
for i in range(0,len(l)):
     for j in range(i,len(l)):
          if l[j]-l[i]>m:
               m=l[j]-l[i]
print("the max profit is: ",m)