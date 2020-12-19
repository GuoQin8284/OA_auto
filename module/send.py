import time

import allure
import logging

from config import BASE_TIME
from driver.action import Action
from module.document_handle import DocumentHandle
from page.menu import MenuFrame


class Send(Action):
    def __init__(self, driver):
        super().__init__(driver)
        self.documentHandle = DocumentHandle(driver)
        self.send = "By.XPATH", "//img[@title='送文']"
        self.all_frame = "By.XPATH", "//div[@class='layui-layer-content']/iframe" # 弹窗的iframe路径
        self.message = "By.XPATH", "//div[contains(text(),'直接发送')]"  # 提示消息的路径
        self.popup_confrim_btn = "By.XPATH", "//div/a[contains(text(),'确定')]"  # 确认按钮
        self.popup_cancel_btn = "By.XPATH", "//div/a[contains(text(),'取消')]"  # 取消按钮
        self.confrim_btn = "XPATH", "//span[@class='queding']/img"
        self.cancel_btn = "XPATH", "//span[@class='quxiao']/img"
        self.wjbt = "By.ID", "wjbt"  # 公文标题
        self.search_box = "ID", "searchtext"  # 搜索框
        self.search_btn = "XPATH", "//b[contains(text(),'搜索')]" # 搜索按钮
        self.select_person = "XPATH", "//div[@id='bxry']/p[contains(text(),'{}')]"
        self.MenuFrame = MenuFrame(driver)

    # 获取提示消息
    @allure.step(title="获取提示消息")
    def __get_message(self):
        try:
            message =  self.find_element(self.message).text
            allure.attach(self.screen_shot(),"截图", allure.attachment_type.PNG)
            return message
        except:
            return ""

    # 点击发送按钮
    @allure.step(title="点击发送按钮")
    def __click_send_btn(self):
        self.find_element(self.send).click()
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)

    # 获取正文标题
    @allure.step(title="获取正文标题")
    def __get_wjbt(self):
        text = self.find_element(self.wjbt).text
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        return text

    # 搜索接收人
    def __search_name(self, name):
        self.input_text(self.search_box, name)
        self.click(self.search_btn)

    # 选取接收人
    def __select_person(self, name):
        self.double_click((self.select_person[0], self.select_person[1].format(name)))

    # 发文流程
    @allure.step(title="发文流程")
    def send_text_flow(self, name):
        wjbt = self.__get_wjbt()
        # self.click_send_btn()
        # time.sleep(BASE_TIME)
        self.MenuFrame.switch_default_content()
        self.driver.switch_to.frame(self.find_element(self.all_frame))
        time.sleep(BASE_TIME)
        message = self.__get_message()
        if name in message:
            logging.info("获取到的提示信息为：{}".format(self.__get_message()))
            self.find_element(self.popup_confrim_btn).click()
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        else:
            if "" != message:
                self.find_element(self.popup_cancel_btn).click()
            self.__search_name(name)
            self.__select_person(name)
            self.click(self.confrim_btn)
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
