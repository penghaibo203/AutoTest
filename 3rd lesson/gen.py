#生成器：生成器表达式、yield，也是个迭代器
#迭代器性质：可迭代的，实现了像next()的方法
#函数里面，只要出现了yield关键字，就自动成为一个生成器
#send()/__next__()/throw()/close()
#next()
#yield 与 return

#print(type((x for x in range(5))))

def myodd():
    n = 1
    while True:
        k = yield n
        n = n + 2
        print(k)

md = myodd()
#print(md.__next__())
print(md.send(None))
md.send("hi, iam k")
md.close()
#md.__next__()



# def mygen():
#     print("before")
#     init = "at first"
#     while True:
#         recev = yield init
#         if recev == "stop":
#             break
#         init = "now is %s" % recev

