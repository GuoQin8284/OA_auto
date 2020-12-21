import json
from unittest.case import TestCase

from parameterized import parameterized

from config import BASE_HOST, BASE_DIR
from driver.action import Action
from driver.data_analysis import data_analysis
from driver.setup_driver import Driver
from page.fwgl.fw_cld import FWCLD_Proxy
from page.fwgl.fw_blz import BLZ_proxy
from page.fwgl.fw_cgx import CGX_proxy
from page.login_page import LoginProxy
from page.fwgl.fw_dbwj import WaitForDoc_proxy
from page.menu import Alert


def lc_data(filename, lcName):
    data_list = data_analysis(filename)
    for i in data_list:
        if i[0]["gwlc"] == lcName:
            data = i[0]["data"]
            print("data",data)
            return data


class Test_demo01(TestCase):

    # pytest方式启动
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        cls.driver.set_auto_quit(1)
        cls.get_driver = cls.driver.get_driver()  # 获取driver对象
        cls.get_driver.get(BASE_HOST)  # 打开网页
        cls.action = Action(cls.get_driver)  # 初始化action类
        cls.DocumentProxy = FWCLD_Proxy(cls.get_driver)  # 初始化
        cls.login = LoginProxy(cls.get_driver)
        cls.login.Login("hcadmin", "123456")
        cls.driver.set_auto_quit(0)
        cls.cgx = CGX_proxy(cls.get_driver)
        cls.Alert = Alert(cls.get_driver)
        cls.blz = BLZ_proxy(cls.get_driver)
        cls.fwdb = WaitForDoc_proxy(cls.get_driver)

    def setUp(self):
        self.get_driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()

    # 发文流程
    def test01_send_text(self):
        data = lc_data("fwgl_data.json", "拟稿")
        bt_text = data["bt_name"]
        zsdw_name = data["zsdw_name"]
        csdw_name = data["csdw_name"]
        rec_name = data["rec_name"]
        next_gwlc = data["next_gwlc"]
        self.DocumentProxy.into_document()  # 进入发文拟稿页面
        self.DocumentProxy.input_bt_proxy(bt_text)  # 输入发文标题
        self.DocumentProxy.select_zsdw(zsdw_name)  # 选择主动单位
        self.DocumentProxy.select_csdw(csdw_name)  # 选择抄送单位
        res_file = self.DocumentProxy.add_fujian(r"D:\report_data2.txt")
        assert res_file
        res_rop = self.DocumentProxy.sign_readOpinion("请审批")
        assert res_rop
        self.DocumentProxy.send_proxy(rec_name, next_gwlc)  # 发送给指定的接收人

    # 发文保存流程
    def test02_fwgl_sign_read(self):
        data = lc_data("fwgl_data.json", "部门领导审稿")
        next_gwlc = data["next_gwlc"]
        bt_text = data["bt_name"]
        readOpinion = data["readOpinion"]
        rec_name = data["rec_name"]
        username = data["username"]
        pwd = data["pwd"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.fwdb.into_fwWaitDocPage()
        self.fwdb.into_doc(bt_text)
        self.DocumentProxy.sign_readOpinion(readOpinion)
        self.DocumentProxy.send_proxy(rec_name, next_gwlc)

    def test03_fwgl_sign_read(self):
        data = lc_data("fwgl_data.json", "办公室核稿")
        next_gwlc = data["next_gwlc"]
        bt_text = data["bt_name"]
        readOpinion = data["readOpinion"]
        rec_name = data["rec_name"]
        username = data["username"]
        pwd = data["pwd"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.fwdb.into_fwWaitDocPage()
        self.fwdb.into_doc(bt_text)
        self.DocumentProxy.sign_readOpinion(readOpinion)
        self.DocumentProxy.send_proxy(rec_name, next_gwlc)

    def test04_fwgl_sign_read(self):
        data = lc_data("fwgl_data.json", "领导签发")
        bt_text = data["bt_name"]
        readOpinion = data["readOpinion"]
        rec_name = data["rec_name"]
        username = data["username"]
        pwd = data["pwd"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.fwdb.into_fwWaitDocPage()
        self.fwdb.into_doc(bt_text)
        self.DocumentProxy.sign_readOpinion(readOpinion)
        self.DocumentProxy.send_proxy(rec_name)

    # 拟稿页面必填项测试
    def test05_save_none(self):
        self.login.switch_loginUser("hcadmin", "123456")
        self.DocumentProxy.into_document()  # 进入发文拟稿页面
        text = self.DocumentProxy.save_document()  # 保存发文
        self.assertIn("标题不能为空", text)

    # 发文删除
    def test06_delete_cgx(self):
        bt = "这是标题，测试保存"
        self.cgx.into_fwcgx()
        self.cgx.delete_doc(bt)
        assert self.cgx.is_delete_success(bt)

    # 从草稿箱打开发文
    def test07_cgx_intoDoc(self,bt="这是测试01"):
        self.cgx.into_fwcgx()
        self.cgx.into_doc(bt)
        assert self.DocumentProxy.get_cldbt()

    # 从办理中页面打开发文
    def test08_blz_intoDoc(self,bt="这是测试01"):
        self.blz.into_fwbzl()
        self.blz.into_doc(bt)
        assert self.DocumentProxy.get_cldbt()

    # 从办理中页面删除发文
    def test09_blz_deleteDoc(self,bt="这是测试01"):
        self.blz.into_fwbzl()
        self.blz.delete_doc(bt)
        assert self.blz.is_delete_success(bt)

    def test10_IntoWaitForDoc(self):
        self.login.switch_loginUser(username="mj", pwd="%Aa123456789")
        self.fwdb.into_fwWaitDocPage()
        self.fwdb.into_doc(bt="安慰法")
        result = self.DocumentProxy.sign_readOpinion("同意！")
        assert result
