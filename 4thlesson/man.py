# 数据、方法、属性，区分class和object，类和对象的区别
# 类的方法：类方法，实例方法，静态方法
# public private proteced
# 模块级的私有化，私有变量__
# from man import *
# 类，模块，包
# import math
# from pkg1 import *

class Human():
    '''
    This is my Human code
    '''
    name = "zhangsan"
    #__slots__ = ("__name")

    def __init__(self, name):
        self.__name = name

    def callphone(self):
        print(self.__name)

    @classmethod
    def myclasscallphone(cls):
        print(cls.name)

    @staticmethod
    def mystaticcallphone():
        print("i am a static function")


# __name__
# __bases__
# __doc__
# __dict__
# __module__
# __class__
# print(Human.__name__)
# print(Human.__dict__)
#
# man1 = Human("lisi")
# # print(man1.name)
# man1.callphone()
#
# man2 = Human("wangwu")
# # print(man2.name)
# man2.callphone()
#
# # print(Human.name)
# Human.myclasscallphone()
# Human.mystaticcallphone()
# man1.mystaticcallphone()

man1 = Human("lisi")
man2 = Human("zhaoqi")
# print(man1.__name)
# print(Human.__dict__)
print(dir(man1))
man1.age = 10
print(dir(man1))
print(dir(man2))


# 槽位

# _类名+原来的名字
# man1._Human__name = "zhengxiao"
# print(man1._Human__name)
# a = "let"

# 类的继承写法，单一继承
# 多重继承
class Woman(Human):
    pass
