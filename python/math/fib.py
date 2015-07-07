# Fibonacci number using Memoization

def _fib(n, cache):
    if n in cache:
        return cache[n]
    cache[n] = 1 if n < 2 else _fib(n-1) + _fib(n-2)
    return cache[n]

def fib(n):
    return _fib(n, {0:0})