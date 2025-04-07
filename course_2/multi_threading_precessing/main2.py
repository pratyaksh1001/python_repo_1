from concurrent.futures import  ProcessPoolExecutor
import time


def factorial(n):
    if n == 1:
        return 1
    time.sleep(1)
    return n*factorial(n-1)
def __main__():
    with ProcessPoolExecutor(3) as executer:
        res=executer.map(factorial,[5,6,7])


if __name__==__main__():
    __main__()