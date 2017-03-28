'''
Created on Mar 27, 2017

@author: patir
'''
'''

@author: patir
'''
def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

print(fib(50))