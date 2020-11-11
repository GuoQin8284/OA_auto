import unittest

from HTMLTestRunner import HTMLTestRunner
from script import Test_demo01

suites = unittest.TestSuite()
suites.addTest(unittest.makeSuite(Test_demo01))

with open("./report/report.html","wb") as f:
    runner = HTMLTestRunner(stream=f,title="OA自动化测试——发文流程",description="Chrome浏览器")
    runner.run(suites)