#函数式编程，命令式编程fp
#y = f(x) x 自变量 y 因变量
#高阶函数，函数名作为参数传入

def my_len(f, a, b):
    return f(a) + f(b)

print(type(my_len))
#my_len()
#Python函数简单可视为：函数名+()
#[1,2,3]
#"abcdefg"

print(my_len(len, [1,2,3], "abcdefg"))





