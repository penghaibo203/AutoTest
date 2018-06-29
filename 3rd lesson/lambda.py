#匿名函数
from functools import *

print(type(lambda x: x*x))

#0~200 所有奇数的平方的和

sum = reduce(lambda x, y: x+y, [x for x in range(1, 200, 2)])

print(sum)

mycalc = lambda x: x*x
print(mycalc(7))


