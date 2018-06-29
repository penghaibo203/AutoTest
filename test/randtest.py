import random

menu = ["韭黄炒蛋", "烤鸭", "杀猪菜"]

a = random.choice(menu)
print(a)

b = random.sample(menu, 2)
print(b)
random.shuffle(menu)
print(menu)
