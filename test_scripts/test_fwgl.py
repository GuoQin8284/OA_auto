import json
from unittest.case import TestCase

from parameterized import parameterized

from config import BASE_HOST
from driver import data_analysis
from driver.action import Action
from driver.analysis_function import analysis_data_func
from driver.setup_driver import Driver
# 读取测试数据
from page.Document_process import DocumentProxy
from page.login_page import LoginProxy


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


    def setUp(self):
        self.get_driver = self.driver.get_driver()
        self.get_driver.get(BASE_HOST)
        self.action = Action(self.get_driver)
        self.DocumentProxy = DocumentProxy(self.get_driver)
        self.login = LoginProxy(self.get_driver)
        self.login.Login("admin","123456")



    @parameterized.expand(data_analysis.data_analysis("send_text01.json"))
    def test01_send_text(self,data):
        bt_text = data["bt_name"]
        zsdw_name = data["zsdw_name"]
        csdw_name = data["csdw_name"]
        rec_name = data["rec_name"]
        print("bt_text:",bt_text)
        print("zsdw_name:",zsdw_name)
        print("csdw_name:",csdw_name)
        print("rec_name:",rec_name)
        self.DocumentProxy.into_document()
        self.DocumentProxy.input_bt_proxy(bt_text)
        self.DocumentProxy.select_zsdw(zsdw_name)
        self.DocumentProxy.select_csdw(csdw_name)
        self.DocumentProxy.send_proxy(rec_name)


