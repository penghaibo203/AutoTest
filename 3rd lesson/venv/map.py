#map reduce filter
import functools
#from functools import *

def myfunc(x):
    return x*x

alist = [1, 7, 9 ,11]
it1 = map(myfunc, alist)
print(list(it1))

def myfunc2(x, y):
    return x + y

#print(reduce(myfunc2, alist))
print(functools.reduce(myfunc2, alist))

def myfunc3(x):
    return x < 10

it2 = filter(myfunc3, alist)
print(list(it2))

