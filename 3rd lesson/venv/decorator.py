#装饰器：
# 是一个带有返回函数的高阶函数，进一步地说，是一个以函数作为参数并返回了一个替代函数的可执行函数
#语法糖
def plusone(func):
    def inner():
        #print("before")
        ret = func() + 1
        return ret
    return inner

@plusone
def foo():
    return 1

# de = outer(foo)
# print(de())

print(foo())
# foo = outer(foo)
# print(foo())

