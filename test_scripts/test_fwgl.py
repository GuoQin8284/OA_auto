import json
from unittest.case import TestCase

import allure
from parameterized import parameterized

from config import BASE_HOST
from driver import data_analysis
from driver.action import Action
from driver.analysis_function import analysis_data_func
from driver.setup_driver import Driver
# 读取测试数据
from page.Document_process import DocumentProxy
from page.fwcgx import CGX_proxy
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
    def setUpClass(cls):
        cls.driver = Driver
        cls.driver.set_auto_quit(1)
        cls.get_driver = cls.driver.get_driver()
        cls.get_driver.get(BASE_HOST)
        cls.action = Action(cls.get_driver)
        cls.DocumentProxy = DocumentProxy(cls.get_driver)
        cls.login = LoginProxy(cls.get_driver)
        cls.login.Login("admin", "123456")
        cls.driver.set_auto_quit(1)
        cls.cgx = CGX_proxy(cls.get_driver)

    def setUp(self):
        self.get_driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()


    # 发文流程

    # @parameterized.expand(data_analysis.data_analysis("send_text01.json"))
    # def test01_send_text(self,data):
    #     bt_text = data["bt_name"]
    #     zsdw_name = data["zsdw_name"]
    #     csdw_name = data["csdw_name"]
    #     rec_name = data["rec_name"]
    #     self.DocumentProxy.into_document()  # 进入发文拟稿页面
    #     self.DocumentProxy.input_bt_proxy(bt_text)  # 输入发文标题
    #     self.DocumentProxy.select_zsdw(zsdw_name)  # 选择主动单位
    #     self.DocumentProxy.select_csdw(csdw_name)  # 选择抄送单位
    #     self.DocumentProxy.send_proxy(rec_name)  # 发送给指定的接收人
    #
    #
    # # 发文保存流程
    #
    # @parameterized.expand(data_analysis.data_analysis("send_text01.json"))
    # def test02_save(self,data):
    #     bt_text = data["bt_name"]
    #     zsdw_name = data["zsdw_name"]
    #     csdw_name = data["csdw_name"]
    #     rec_name = data["rec_name"]
    #     self.DocumentProxy.into_document()  # 进入发文拟稿页面
    #     self.DocumentProxy.input_bt_proxy(bt_text)  # 输入发文标题
    #     self.DocumentProxy.select_zsdw(zsdw_name)  # 选择主动单位
    #     self.DocumentProxy.select_csdw(csdw_name)  # 选择抄送单位
    #     self.DocumentProxy.save_document()
    #     assert self.DocumentProxy.get_cgx_status(bt_text)

    def test03_delete_cgx(self):
        self.cgx.into_fwcgx()
        self.cgx.delete_doc()


