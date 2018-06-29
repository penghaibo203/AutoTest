def consumer():
    last = ''
    while True:
        print(last)
        receival = yield last
        if receival is not None:
            print('Consume %d' % receival)
            last = "last"


def producer(gen, n):
    next(gen)
    x = 0
    while x < n:
        x += 1
        print('Produce %d' % x)
        last = gen.send(x)
    gen.close()


gen = consumer()

print(producer(gen, 5))
