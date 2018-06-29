#闭包
# 1, 3, 5
# 1, 11, 90, 56
# f(1, 3, 5)
# f(1, 11, 90, 56)

def my_add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(my_add(1, 3, 5))
#print(args)
#print(my_add(1, 11, 90, 56, 97))


def my_lazy_add(*args):
    def my_add():
        sum = 0
        for item in args:
            sum += item
        return sum
    return my_add

f = my_lazy_add(1, 3, 5)
#print(args)
print(f)
print(f())







