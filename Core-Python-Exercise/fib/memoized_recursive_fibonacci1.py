'''
Created on Mar 27, 2017

@author: patir
'''


__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return __fib_cache[n]
    
if __name__=="__main__":
    print(fib(50))
    print(__fib_cache)