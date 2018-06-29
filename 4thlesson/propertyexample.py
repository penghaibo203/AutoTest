#属性
# class CaiWu():
#     def __init__(self, money):
#         self.money = money
#
#     def toRMB(self):
#         return self.money * 6.5
#
# ls1 = CaiWu(120)
# ls1toRMB = ls1.toRMB()
# print(ls1toRMB)
# ls1.money
# ls1.money = 200
# print(ls1.toRMB())


# class CaiWu():
#     def __init__(self, money=0):
#         self.set_money(money)
#
#     def toRMB(self):
#         return self._money * 6.5
#
#     def get_money(self):
#         return self._money
#
#     def set_money(self, newmoney):
#         if newmoney < 0:
#             raise ValueError("can not less than zero")
#         self._money = newmoney
#
# ls2 = CaiWu(120)
# print(ls2.get_money())



#使用property()，以函数的形式创建一个属性，函数的参数填入访问器函数名，以支持.号访问
# class CaiWu():
#     def __init__(self, money=0):
#         self.money = money
#
#     def toRMB(self):
#         return self.money * 6.5
#
#     def get_money(self):
#         return self._money
#
#     def set_money(self, newmoney):
#         if newmoney < 0:
#             raise ValueError("can not less than zero")
#         self._money = newmoney
#
#     money = property(get_money, set_money)
#
#
# ls3 = CaiWu(140)
# ls3.money = -180
# print(ls3.money)


#通过装饰器语法来直接创建属性，实质是将一个实例方法“伪装”成与其同名的数据属性，以支持.号访问，同时可添加访问限制
class CaiWu():
    def __init__(self, money=0):
        self.money = money

    def toRMB(self):
        return self.money * 6.5

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, newmoney):
        if newmoney < 0:
            raise ValueError("can not less than zero")
        self._money = newmoney


ls4 = CaiWu(100)
#print(ls4.toRMB())
ls4.money = 180
#print(ls4.toRMB())
print(ls4.money)
