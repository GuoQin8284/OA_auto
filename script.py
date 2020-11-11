import json
from unittest.case import TestCase
import time
from driver.analysis_function import analysis_data_func
from parameterized import parameterized

from driver.setup_driver import Driver


def data(file):
    with open("./test_data/{}" .format(file), mode="r", encoding="utf-8") as f:
        data = (json.load(f),)
        return data

class Test_demo01(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        cls.driver.set_auto_quit(1)
        cls.get_driver = cls.driver.get_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()

    # 登录流程测试用例
    @parameterized.expand([data("login.json")])
    def test01_login(self,loginData):
        print(loginData)
        print(type(loginData))
        text = analysis_data_func(self.get_driver,loginData)
        self.assertIn("当前用户",text)

    # 发文流程测试用例
    @parameterized.expand([data("send_text.json")])
    def test02_sendText(self,sendData):
        time.sleep(2)
        result = analysis_data_func(self.get_driver,sendData)
        print("result:",result)
        self.assertTrue(result)
