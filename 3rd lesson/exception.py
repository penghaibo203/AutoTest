#异常和错误

# def foo():
#     print(1/0)
#
# def foo2():
#     foo()
#
# foo2()
#try/except/else/finally
#raise

# fh = open("txttest.txt", "r")
# fh.write("hello world")
# fh.close()

#IOError/TypeError/ValueError/KeyError

try:
    fh = open("txttest.txt", "r")
    fh.write("hello world")
except TypeError as TE:
    print("oh my god")
except ValueError as VE:
    pass
except IOError as IOE:
    pass
else:
    raise IOError
finally:
    fh.close()

