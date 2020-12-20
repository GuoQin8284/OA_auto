# 读取测试数据
import json
from unittest import TestCase

from config import BASE_HOST, BASE_DIR
from driver.action import Action
from driver.setup_driver import Driver
from page.login_page import LoginProxy
from page.menu import Alert
from page.swgl.sw_blz import SWBLZProxy
from page.swgl.sw_cgx import SWCGXProxy
from page.swgl.sw_cld import SWCLDProxy
from page.swgl.sw_dbwj import SWDBProxy


def data_read(file):
    with open(BASE_DIR+"/test_data/{}" .format(file), mode="r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = [(x,) for x in data]
        # print(data_list)
        return data_list
# if __name__ == "__main__":
#     data_read("send_text_save.json")
#     data_read("send_text.json")


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

    def setUp(self):
        self.get_driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()

    def test01_info_swgl(self):
        self.swcld.into_swcld()
        self.swcld.input_swgl_info("上级单位", ("上级单位", "交通厅"), "2020-12-18", "急",
                                  "10", "test_007", "2020-12-25", "2020-12-23", "这是收文测试01",
                                  "单位文", "D:\c.jpg")
        self.swcld.sign_readOpinion("同意哈哈哈哈哈哈")
        self.swcld.add_fujian(r"D:\c.jpg")
        self.swcld.save_document()
        self.swcgx.into_doc("这是收文测试01")
        self.swcld.send_proxy("管晓峰")

    def test02_delete_cgx(self):
        self.swcgx.into_swcgx()
        self.swcgx.delete_doc("这是收1文")
        self.swcgx.into_doc("asdf")
        self.swblz.into_Swbzl()
        result = self.swblz.getByDocCurrentPerson("菜单创建步骤及菜单权限配置步骤")
        self.swblz.into_doc("菜单创建步骤及菜单权限配置步骤")
        print("result:", result)

    def test03_create_dbwj(self):
        self.login.switch_loginUser(username="guanxf", pwd="123456")
        self.swdb.into_Swbzl()
        self.swdb.into_doc("这是收文测试01")
        self.swcld.sign_readOpinion("同意。。。。")

