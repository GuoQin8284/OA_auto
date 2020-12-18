import time

import allure
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException

from config import BASE_TIME
from driver.log_method import log_method
from driver.action import Action


class MenuFrame(Action):

    def __init__(self,driver):
        super().__init__(driver)
        self.__doc_manager = "公文管理"  # 公文管理元素
        self.__left_iframe = "left"  # 左边菜单iframe
        self.__right_iframe = "rfm"  # 右边内容框iframe

    # 切换iframe到左侧列表
    def switch_left_iframe(self):
        self.driver.switch_to.frame(self.__left_iframe)

    # 切换iframe到右侧列表
    def switch_right_iframe(self):
        self.driver.switch_to.frame(self.__right_iframe)

    # 切换iframe退回上一步
    def switch_parent_iframe(self):
        self.driver.switch_to.parent_frame()

    # 重置iframe
    def switch_default_content(self):
        self.driver.switch_to.default_content()


class Alert(Action):

    def __init__(self,driver):
        super().__init__(driver)

    # 切换到alert弹窗
    def switch_alert(self):
        ele = self.driver.switch_to.alert
        return ele

    # 弹出框确认
    def alert_accept(self):
        try:
            self.switch_alert().accept()
            time.sleep(BASE_TIME)
        except NoAlertPresentException:
            pass

    # 弹出框取消
    def alert_dismiss(self):
        try:
            self.switch_alert().dismiss()
            time.sleep(BASE_TIME)
        except NoAlertPresentException:
            pass

    # 获取弹出框中的文本
    def get_alert_text(self):
        try:
            alert_text = self.switch_alert().text
            self.alert_accept()
            allure.attach(self.screen_shot(), "弹框截图", allure.attachment_type.PNG)
            return alert_text
        except NoAlertPresentException:
            return False

    # 输入内容到弹出框中
    def alert_input_text(self,text):
        self.switch_alert().Send_keys(text)