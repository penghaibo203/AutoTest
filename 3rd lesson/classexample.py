#属性，功能（方法）
#超类和子类
class Dog():
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
    def buger(self):
        print("wangwang")

adog = Dog(80, 120)
adog.buger()

print(adog.__dir__())
