# 读取测试数据
import json
from unittest import TestCase

from config import BASE_HOST
from driver.action import Action
from driver.data_analysis import data_analysis
from driver.setup_driver import Driver
from page.login_page import LoginProxy
from page.menu import Alert
from page.swgl.sw_blz import SWBLZProxy
from page.swgl.sw_cgx import SWCGXProxy
from page.swgl.sw_cld import SWCLDProxy
from page.swgl.sw_dbwj import SWDBProxy
from page.swgl.swgl_yzj import SWYBJProxy


def lc_data(filename, lcName):
    data_list = data_analysis(filename)
    for i in data_list:
        if i[0]["gwlc"] == lcName:
            data = i[0]["data"]
            print("data", data)
            return data


class Test_demo01(TestCase):

    # pytest方式启动
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver
        cls.driver.set_auto_quit(0)
        cls.get_driver = cls.driver.get_driver()
        cls.get_driver.get(BASE_HOST)

        cls.action = Action(cls.get_driver)
        cls.login = LoginProxy(cls.get_driver)
        cls.login.Login("hcadmin", "123456")
        cls.Alert = Alert(cls.get_driver)
        cls.swcld = SWCLDProxy(cls.get_driver)
        cls.swcgx = SWCGXProxy(cls.get_driver)
        cls.swblz = SWBLZProxy(cls.get_driver)
        cls.swdb = SWDBProxy(cls.get_driver)
        cls.swybj = SWYBJProxy(cls.get_driver)

    def setUp(self):
        self.get_driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()

    def test01_swgl_lc01(self):
        data = lc_data(filename="swgl_data.json", lcName="收文登记")
        swh = data["收文号"]
        lwdw = data["来文单位"]
        swrq = data["收文日期"]
        jjcd = data["紧急程度"]
        fs = data["份数"]
        gwbh = data["公文编号"]
        blsx = data["办理时限"]
        cbsx = data["催办时限"]
        gwbt = data["公文标题"]
        swlx = data["收文类型"]
        sczw = data["上传正文"]
        ywyj = data["阅文意见"]
        fujian = data["附件"]
        rec_name = data["接收人"]
        next_lcmc = data["下一个节点"]
        self.swcld.into_swcld()
        self.swcld.input_swgl_info(swh=swh, lwdw=lwdw, swrq=swrq, jjcd=jjcd,
                                   fs=fs, gwbh=gwbh, blsx=blsx, cbsx=cbsx, gwbt=gwbt,
                                   swlx=swlx, sczw=sczw)  # 输入收文信息
        self.swcld.sign_readOpinion(ywyj)  # 签署阅文意见
        self.swcld.add_fujian(fujian)  # 添加附件
        self.swcld.save_document()  # 保存收文
        self.swcgx.into_doc(gwbt)  # 进入草稿箱页面，然后从草稿箱页面打开收文
        self.swcld.send_proxy(rec_name=rec_name, lcname=next_lcmc)  # 发送给指定的人

    def test02_swgl_lc02(self):
        data = lc_data(filename="swgl_data.json", lcName="部门文书接收")
        username = data["用户名"]
        pwd = data["密码"]
        gwbt = data["公文标题"]
        ywyj = data["阅文意见"]
        rec_name = data["接收人"]
        next_lcmc = data["下一个节点"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.swdb.into_Swdb()
        self.swdb.into_doc(gwbt)
        self.swcld.sign_readOpinion(ywyj)  # 签署阅文意见
        self.swcld.send_proxy(rec_name=rec_name, lcname=next_lcmc)  # 发送给指定的人

    def test03_swgl_lc03(self):
        data = lc_data(filename="swgl_data.json", lcName="部门内办理")
        username = data["用户名"]
        pwd = data["密码"]
        gwbt = data["公文标题"]
        ywyj = data["阅文意见"]
        rec_name = data["接收人"]
        next_lcmc = data["下一个节点"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.swdb.into_Swdb()  # 进入收文待办
        self.swdb.into_doc(gwbt)  # 根据标题进入公文处理单页面
        self.swcld.sign_readOpinion(ywyj)  # 签署阅文意见
        self.swcld.send_proxy(rec_name=rec_name, lcname=next_lcmc)  # 发送给指定的人

    def test04_swgl_lc04(self):
        data = lc_data(filename="swgl_data.json", lcName="部门领导审核")
        username = data["用户名"]
        pwd = data["密码"]
        gwbt = data["公文标题"]
        ywyj = data["阅文意见"]
        rec_name = data["接收人"]
        next_lcmc = data["下一个节点"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.swdb.into_Swdb()
        self.swdb.into_doc(gwbt)
        self.swcld.sign_readOpinion(ywyj)  # 签署阅文意见
        self.swcld.send_proxy(rec_name=rec_name, lcname=next_lcmc)  # 发送给指定的人

    def test05_swgl_lc05(self):
        data = lc_data(filename="swgl_data.json", lcName="办结")
        username = data["用户名"]
        pwd = data["密码"]
        gwbt = data["公文标题"]
        ywyj = data["阅文意见"]
        rec_name = data["接收人"]
        next_lcmc = data["下一个节点"]
        self.login.switch_loginUser(username=username, pwd=pwd)
        self.swdb.into_Swdb()
        self.swdb.into_doc(gwbt)
        self.swcld.sign_readOpinion(ywyj)  # 签署阅文意见
        self.swcld.end()
        assert self.swcld.is_end_success(gwbt)

    # def test02_delete_cgx(self):
    #     self.swcgx.into_swcgx()
    #     self.swcgx.delete_doc("这是收1文")
    #     self.swcgx.into_doc("asdf")
    #     self.swblz.into_Swbzl()
    #     result = self.swblz.getByDocCurrentPerson("菜单创建步骤及菜单权限配置步骤")
    #     self.swblz.into_doc("菜单创建步骤及菜单权限配置步骤")
    #     print("result:", result)
    #
    # def test03_create_dbwj(self):
    #     self.login.switch_loginUser(username="mj", pwd="%Aa123456789")
    #     self.swdb.into_Swbzl()
    #     self.swdb.into_doc("这是收文测试01")
    #     self.swcld.sign_readOpinion("同意。。。。")

    # def test_bj(self):
    #     self.swcld.into_swcld()
    #     self.swcld.click_bj()

