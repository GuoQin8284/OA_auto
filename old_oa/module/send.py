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
        self.__documentHandle = DocumentHandle(driver)
        self.__send = "By.XPATH", "//img[@title='送文']"
        self.__all_frame = "By.XPATH", "//div[@class='layui-layer-content']/iframe" # 弹窗的iframe路径
        self.__message = "By.XPATH", "//div[contains(text(),'直接发送')]"  # 提示消息的路径
        self.__popup_confrim_btn = "By.XPATH", "//div/a[contains(text(),'确定')]"  # 确认按钮
        self.__popup_cancel_btn = "By.XPATH", "//div/a[contains(text(),'取消')]"  # 取消按钮
        self.__confrim_btn = "XPATH", "//span[@class='queding']/img"  # 弹窗确定按钮
        self.__cancel_btn = "XPATH", "//span[@class='quxiao']/img"  # 弹窗取消按钮
        self.__wjbt = "By.ID", "wjbt"  # 公文标题
        self.__search_box = "ID", "searchtext"  # 搜索框
        self.__search_btn = "XPATH", "//b[contains(text(),'搜索')]" # 搜索按钮
        self.__person = "XPATH", "//div[@id='bxry']/p[contains(text(),'{}')]"  # 选择人员
        self.__select_lcxz = "XPATH", "//table[@id='lcfz']/tbody/tr/td/span/input" # 流程选择
        self.__MenuFrame = MenuFrame(driver)

    # 获取提示消息
    @allure.step(title="获取提示消息")
    def __get_message(self):
        try:
            message =  self.find_element(self.__message).text
            allure.attach(self.screen_shot(),"截图", allure.attachment_type.PNG)
            return message
        except:
            return ""

    # 点击发送按钮
    @allure.step(title="点击发送按钮")
    def __click_send_btn(self):
        self.find_element(self.__send).click()
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)

    # 获取正文标题
    @allure.step(title="获取正文标题")
    def __get_wjbt(self):
        text = self.find_element(self.__wjbt).text
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        return text

    # 搜索接收人
    def __search_name(self, name):
        self.input_text(self.__search_box, name)
        self.click(self.__search_btn)

    # 选取接收人
    def __select_person(self, name):
        self.double_click((self.__person[0], self.__person[1].format(name)))

    def __select_lcxx(self,lcname=None):
        if lcname:
            eles = self.find_elements(self.__select_lcxz)
            cur_lc = [x for x in eles if x.get_attribute("value").strip() == lcname][0]
            get_lc_state = cur_lc.is_selected()
            if get_lc_state is False:
                cur_lc.click()
        else:
            pass

    # 发文流程
    @allure.step(title="发文流程")
    def send_text_flow(self, name, lcname=None):
        wjbt = self.__get_wjbt()
        # self.click_send_btn()
        # time.sleep(BASE_TIME)
        self.__MenuFrame.switch_default_content()
        self.driver.switch_to.frame(self.find_element(self.__all_frame))
        time.sleep(BASE_TIME)
        message = self.__get_message()
        if name in message:
            logging.info("获取到的提示信息为：{}".format(self.__get_message()))
            self.find_element(self.__popup_confrim_btn).click()
            time.sleep(BASE_TIME)
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
            time.sleep(BASE_TIME)
        else:
            if "" != message:
                self.find_element(self.__popup_cancel_btn).click()
                time.sleep(BASE_TIME)
            self.__select_lcxx(lcname)
            time.sleep(BASE_TIME)
            self.__search_name(name)
            time.sleep(BASE_TIME)
            self.__select_person(name)
            time.sleep(BASE_TIME)
            self.click(self.__confrim_btn)
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
            time.sleep(BASE_TIME)
