#浅拷贝和深拷贝
import copy

lista = [1, 3, 5, [4, 7]]
listb = lista

# lista[0] = 100
# print(lista)
# print(listb)

#浅拷贝&#深拷贝
listc = copy.copy(lista)
listd = copy.deepcopy(lista)
# print(listc)
lista[0] = 110
print(lista)
print(listb)
print(listc)
print(listd)

# lista[3] = [2, 10]
lista[3].append(9)
print(lista)
print(listb)
print(listc)
print(listd)




