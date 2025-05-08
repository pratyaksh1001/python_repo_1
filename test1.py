#   matrix sum
import time
start=time.time()
n=1000000000
x=0
for i in range(n):
     x+=1
print(x)
end=time.time()
print(end-start)