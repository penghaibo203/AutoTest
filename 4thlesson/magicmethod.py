#魔法方法：__xxxx__()，就是魔法方法
__init__()

__new__()
__len__()
__getitem__()
__setitem__()
#for i in iter(自定义对象)
__next__()
__iter__()
#上下文管理
__enter__()
__exit__()

with open("/usr/bin/python.txt", "wb") as f:
    print(f.readline())

#超类A，子类B
A.__init__()
B.__init__():
    super().__init__()
    继续初始化B自己的东西


alist = []
alist.append(1)
alist.append(2)
print(alist)
alist[0]
