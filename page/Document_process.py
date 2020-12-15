# 发文处理单页面
import logging
import time

from selenium.webdriver.support.select import Select

from config import BASE_TIME
from driver.log_method import log_method
from driver.action import Action
from module.select_department import SelectDepartment
from module.send import Send
from page.menu import MenuFrame


class Document(Action):
    def __init__(self,driver):
        super().__init__(driver)
        self.search_department = SelectDepartment(driver)
        self.send_flow = Send(driver)
        self.send_bt_box = "ID","wjbt"  # 发文标题输入框
        self.zsdw = "ID","zsdw"  # 主送单位
        self.csdw = "XPATH","//textarea[@title='双击选择抄送单位']"  # 抄送单位
        self.mj = "ID","mj"  # 密级下拉选择框
        self.fs = "ID","fs"  # 份数输入框
        self.sava_btn = "XPATH","//img[@title='保存']"  # 保存按钮
        self.fujian = "XPATH","//img[@title='附件']"  # 附件按钮
        self.readOpinion = "XPATH", "//img[@title='阅文意见']"  # 阅文意见按钮
        self.send = "XPATH", "//img[@title='送文']"  # 发送按钮
        self.back = "XPATH", "//img[@title='返回']"  # 返回按钮

    # 点击返回按钮
    def click_back(self):
        self.click(self.back)
    # 点击保存按钮
    def click_save(self):
        self.click(self.sava_btn)
    # 点击阅文意见按钮
    def click_readOpinion(self):
        self.click(self.readOpinion)
    # 点击发送按钮
    def click_send(self):
        self.click(self.send)
    # 输入份数，num表示份数
    def input_fs(self,num):
        self.input_text(self.fs,num)
    # 双击主送单位
    def double_zsdw(self):
        self.double_click(self.zsdw)
    # 双击抄送单位
    def double_csdw(self):
        print("self.csdw:",self.csdw)
        self.double_click(self.csdw)
    # 选择密级等级
    def select_mj(self,text):
        Select(self.find_element(self.mj)).select_by_visible_text(text)
    # 输入标题
    def input_bt_text(self,text):
        self.input_text(self.send_bt_box,text)


class DocumentProxy(Document):
    def __init__(self,driver):
        super().__init__(driver)
        self.MenuFrame = MenuFrame(driver)

    # 进入拟稿页面
    def into_document(self):
        self.contains_text("公文管理").click()  # 点击公文管理
        time.sleep(BASE_TIME)
        self.MenuFrame.switch_left_iframe()
        self.contains_text("发文管理").click()  # 点击发文管理菜单
        time.sleep(BASE_TIME)
        self.contains_text("发文拟稿").click()  # 点击发文拟稿菜单，进入拟稿页面

    # 输入文章标题
    def input_bt_proxy(self,text):
        self.MenuFrame.switch_default_content()
        self.MenuFrame.switch_right_iframe()
        time.sleep(BASE_TIME)
        self.input_bt_text(text)  # 输入公文标题

    # 选择主送单位
    def select_zsdw(self,zsdw_name):
        self.MenuFrame.switch_default_content()
        self.MenuFrame.switch_right_iframe()
        self.double_zsdw()  # 双击主送单位输入框
        time.sleep(BASE_TIME)
        self.search_department.SearchName(zsdw_name)  # 调用部门选择方法，选择部门
        time.sleep(BASE_TIME)


    # 选择抄送单位
    def select_csdw(self,csdw_name):
        self.MenuFrame.switch_default_content()
        self.MenuFrame.switch_right_iframe()
        self.double_csdw()  # 双击抄送单位输入框
        time.sleep(BASE_TIME)
        self.search_department.SearchName(csdw_name)  # 调用部门选择方法，选择部门
        time.sleep(BASE_TIME)

    # 发送流程（选择发文人发送）
    def send_proxy(self,rec_name):
        self.MenuFrame.switch_default_content()
        self.MenuFrame.switch_right_iframe()
        self.click_send()
        time.sleep(BASE_TIME)
        self.send_flow.send_text_flow(rec_name)
        self.driver.switch_to.default_content()
