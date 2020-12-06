import json
from unittest.case import TestCase
import time
import allure

from driver.action import Action
from driver.analysis_function import analysis_data_func, get_host_port
from parameterized import parameterized

from driver.setup_driver import Driver


# 读取测试数据
from module.send_text_save import SendTextSave


def data_read(file):
    with open("./test_data/{}" .format(file), mode="r", encoding="utf-8") as f:

        data = json.load(f)
        data_list = [(x,) for x in data]
        print(data_list)
        return data_list
# if __name__ == "__main__":
#     data_read("send_text_save.json")
#     data_read("send_text.json")


class Test_demo01(TestCase):
    # pytest方式启动
    @classmethod
    def setup_class(cls):
        cls.driver = Driver
        cls.driver.set_auto_quit(1)
        cls.get_driver = cls.driver.get_driver()
        cls.action = Action(cls.get_driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit_driver()

    # unittest方式启动
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = Driver
    #     cls.driver.set_auto_quit(1)
    #     cls.get_driver = cls.driver.get_driver()
    #
    # @classmethod
    # def tearDown_class(cls):
    #     cls.driver.quit_driver()
    #
    # 登录流程测试用例
    @parameterized.expand((data_read("login.json")))
    def test01_login(self,loginData):
        print(loginData)
        print(type(loginData))
        text = analysis_data_func(self.get_driver,loginData)
        self.assertIn("当前用户",text)

    # 发文流程测试用例
    @parameterized.expand(data_read("send_text.json"))
    def test02_sendText(self,sendData):
        time.sleep(2)
        result = analysis_data_func(self.get_driver,sendData)
        print("result:",result)
        self.assertTrue(result)

    # 发文流程测试用例
    @parameterized.expand(data_read("send_text_save.json"))
    def test03_sendText_save(self, sendData):
        url = get_host_port()+ sendData["url"]
        bt_text = sendData["bt_text"]
        result = SendTextSave(self.action).save_text_flow(url,bt_text)  # 调用发文保存流程模块，并保存返回值
        self.assertIn(bt_text,result)  # 将返回的结果与标题文字进行对比断言


