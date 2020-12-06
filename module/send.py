import time

import allure

from config import BASE_TIME
from driver.action import Action
from module.document_handle import DocumentHandle


class Send(Action):
    def __init__(self,driver):
        super().__init__(driver)
        self.documentHandle = DocumentHandle(driver)
        self.send = "By.XPATH","//img[@title='送文']"
        self.all_frame = "By.XPATH", "//div[@class='layui-layer-content']/iframe"
        self.message = "By.XPATH","//div[contains(text(),'直接发送')]"
        self.confrim_btn = "By.XPATH","//a[contains(text(),'确定')]"
        self.cancel_btn = "By.XPATH","//a[contains(text(),'取消')]"
        self.wjbt = "By.ID","wjbt"

    # 获取提示消息
    @allure.step(title="获取提示消息")
    def get_message(self):
        message =  self.find_element(self.message).text
        allure.attach(self.screen_shot(),"截图", allure.attachment_type.PNG)
        print("message:",message)
        return message
    # 点击发送按钮
    @allure.step(title="点击发送按钮")
    def click_send_btn(self):
        self.find_element(self.send).click()
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)

    # 获取正文标题
    @allure.step(title="获取正文标题")
    def get_wjbt(self):
        text = self.find_element(self.wjbt).text
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        return text

    # 发文流程
    @allure.step(title="发文流程")
    def send_text_flow(self,name):
        wjbt = self.get_wjbt()
        # self.click_send_btn()
        # time.sleep(BASE_TIME)
        self.driver.switch_to.frame(self.find_element(self.all_frame))
        time.sleep(BASE_TIME)
        if name in self.get_message():
            self.find_element(self.confrim_btn).click()
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        else:
            self.find_element(self.cancel_btn).click()
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        if (wjbt in self.documentHandle.get_document_titles()[0]) and (name in self.documentHandle.get_current_person()[0]):
            print("创建成功")
            return True
        else:
            print("创建失败")
            return False