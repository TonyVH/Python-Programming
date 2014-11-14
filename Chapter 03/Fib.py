# Fib.py
from math import *

def fib(n):
    a, b = 0, 1
    l = []
    while a < n:
        l.append(a)
        a, b = b, a+b
    num = eval(input('Input the number in the Fibonacci squence you wish to discover: '))
    print(l[num - 1])

fib(factorial(500))

