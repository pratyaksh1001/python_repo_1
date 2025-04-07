import sys
import time
from concurrent.futures import ThreadPoolExecutor

l=[100,101,102]

def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
now=time.perf_counter()
with ThreadPoolExecutor(3) as executer:
    result=executer.map(fact,l)
for i in result:
    print(i)
then=time.perf_counter()
print((then-now)*1000,"ms")