import json
from unittest.case import TestCase

from parameterized import parameterized

from config import BASE_HOST, BASE_DIR
from driver.action import Action
from driver.data_analysis import data_analysis
from driver.setup_driver import Driver
from page.Document_process import DocumentProxy
from page.fw_blz import BLZ_proxy
from page.fwcgx import CGX_proxy
from page.login_page import LoginProxy
from page.menu import Alert


# 读取测试数据
def data_read(file):
    with open(BASE_DIR+"/test_data/{}" .format(file), mode="r", encoding="utf-8") as f:
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
        cls.login.Login("hcadmin", "123456")
        cls.driver.set_auto_quit(0)
        cls.cgx = CGX_proxy(cls.get_driver)
        cls.Alert = Alert(cls.get_driver)
        cls.blz = BLZ_proxy(cls.get_driver)

    def setUp(self):
        self.get_driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()

    # # 发文流程
    # @parameterized.expand(data_analysis("send_text01.json"))
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
    # # 发文保存流程
    # @parameterized.expand(data_analysis("send_text01.json"))
    # def test02_save(self,data):
    #     bt_text = data["bt_name"]
    #     zsdw_name = data["zsdw_name"]
    #     csdw_name = data["csdw_name"]
    #     rec_name = data["rec_name"]
    #     self.DocumentProxy.into_document()  # 进入发文拟稿页面
    #     self.DocumentProxy.input_bt_proxy(bt_text)  # 输入发文标题
    #     self.DocumentProxy.select_zsdw(zsdw_name)  # 选择主动单位
    #     self.DocumentProxy.select_csdw(csdw_name)  # 选择抄送单位
    #     self.DocumentProxy.save_document() # 保存发文
    #     assert self.DocumentProxy.is_save_success(bt_text)

    # 拟稿页面必填项测试
    def test03_save_none(self):
        self.DocumentProxy.into_document()  # 进入发文拟稿页面
        text = self.DocumentProxy.save_document()  # 保存发文
        self.assertIn("标题不能为空", text)


    # # 发文删除
    # def test04_delete_cgx(self):
    #     bt = "这是标题，测试保存"
    #     self.cgx.into_fwcgx()
    #     self.cgx.delete_doc(bt)
    #     assert self.cgx.is_delete_success(bt)
    #
    # # 从草稿箱打开发文
    # def test05_cgx_intoDoc(self,bt="这是测试01"):
    #     self.cgx.into_fwcgx()
    #     self.cgx.into_doc(bt)
    #     assert self.DocumentProxy.get_cldbt()
    #
    # # 从办理中页面打开发文
    # def test06_blz_intoDoc(self,bt="这是测试01"):
    #     self.blz.into_fwbzl()
    #     self.blz.into_doc(bt)
    #     assert self.DocumentProxy.get_cldbt()
    #
    # # 从办理中页面删除发文
    # def test07_blz_deleteDoc(self,bt="这是测试01"):
    #     self.blz.into_fwbzl()
    #     self.blz.delete_doc(bt)
    #     assert self.blz.is_delete_success(bt)
