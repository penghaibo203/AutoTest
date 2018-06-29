#推导式
#列表，字典，集合

#一种Python写法，产生对应的可迭代类型

#[exp for item in collection if condition ]

print([x*x for x in range(10)])
print([x*x for x in range(10) if x % 2 ==0])

a = [[1, 3], [23, 7], [4, 9]]
#b = [1, 3, 23, 7, 4, 9]

c = [x for li in a for x in li]
print(c)

#字典推导式
#{key_exp: value_exp for item in collection if condition}
#{0:0, 1:1, 2:4, ...}

adic = {x: x*x for x in range(10)}
print(adic)

#集合推导式
#{exp for item in collection if condition}

aset = {x for x in range(20) if x % 3 == 0}
print(aset)






