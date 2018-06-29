# ddt, data driver test
import ddt
import unittest
from selenium import webdriver

returndata = []

def get_context(filename='somedata.txt'):
    with open(filename, 'r') as f:
        data = f.readlines()
        for record in data:
            returndata.append(record.strip().split("|"))
    return returndata


@ddt.ddt
class MyCase(unittest.TestCase):
    def setUp(self):
        print("before run")

    def tearDown(self):
        print("after run")

    #@ddt.data([1, 2, 3], [2, 3, 5], "hello")
    @ddt.data(*get_context())
    @ddt.unpack
    def test_print(self, value1, value2, value3):
        print(value1)
        print(value2)
        print(value3)


if __name__ == "__main__":
    unittest.main()
