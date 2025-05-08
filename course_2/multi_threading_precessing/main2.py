#from concurrent.futures import  ProcessPoolExecutor
import time


def factorial(n):
    if n == 1:
        return 1
    time.sleep(1)
    return n*factorial(n-1)


"""def __main__():
    with ProcessPoolExecutor(3) as executer:
        res=executer.map(factorial,[5,6,7,8,9,5,4,3,10,11,12])"""

def test():
    l=[12,]
    for i in l:
        factorial(i)

if __name__=="__main__":
    start = time.time()
    #__main__()
    test()
    end = time.time()
    print((end-start)*1000,"ms")