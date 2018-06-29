import time
import unittest
from test_suites.regsuite import make_suite
from lib.HTMLTestRunner import HTMLTestRunner
from HTMLReport import HTMLReport

if __name__ == "__main__":
    runtime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    reportname = "test_result_{}.html".format(runtime)
    with open("reports/{}".format(reportname), 'wb') as f:
        runner = HTMLTestRunner(stream = f,
                                title='ECshop自动化测试报告',
                                description='CI版本测试结果',
                                verbosity=2
                                )
        runner.run(make_suite())
