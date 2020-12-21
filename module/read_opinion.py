import time

import allure

from config import BASE_TIME
from driver.action import Action
from page.menu import MenuFrame


class ReadOpinion():
    def __init__(self, driver):
        self.__menuFrame = MenuFrame(driver)
        # 第一层frame
        self.__all_frame = "By.XPATH", "//div[@class='layui-layer-content']/iframe"
        # 阅文意见输入框
        self.__content = "By.ID", "TextContent"
        # 确认后打开送文框的单选框
        self.__Radio = "By.ID", "autoLoadSendDlg"
        # 确认按钮
        self.__confirm = "By.ID", "img_qd"
        # 初始化action类
        self.__action = Action(driver)
        # 修改成功的toast提示
        self.__toast = "By.XPATH", '//div[contains(text(),"成功签署意见!")]'

    # 输入阅文意见
    @allure.step(title="输入阅文意见")
    def __input_content(self, text):
        self.__action.input_text(self.__content, text)
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(BASE_TIME)

    # 获取送文单选框的状态
    @allure.step(title="获取送文单选框的状态")
    def __get_radio_state(self):
        state = self.__action.find_element(self.__Radio).is_selected()
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(BASE_TIME)
        return state

    # 点击送文单选框
    @allure.step("点击送文单选框")
    def __click_radio(self):
        self.__action.find_element(self.__Radio).click()
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(BASE_TIME)

    # 点击确认按钮
    @allure.step(title="点击确认按钮")
    def __click_confirm(self):
        self.__action.find_element(self.__confirm).click()
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(BASE_TIME)

    # 获取阅文意见签约成功的toast
    @allure.step(title="获取阅文意见签约成功的toast")
    def __get_toast(self):
        self.__menuFrame.switch_default_content()
        self.__menuFrame.switch_right_iframe()
        toast = self.__action.find_element(self.__toast).text
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(BASE_TIME)
        return toast

    # 输入阅文意见的业务流程
    @allure.step(title="阅文意见的业务流程")
    def signReadOpinion_proxy(self, text, auto=False):
        self.__menuFrame.switch_default_content()
        self.__action.driver.switch_to.frame(self.__action.find_element(self.__all_frame))
        time.sleep(BASE_TIME)
        self.__input_content(text)
        time.sleep(BASE_TIME)
        state = self.__get_radio_state()
        time.sleep(BASE_TIME)
        if state and (auto is False):
            self.__click_radio()
            time.sleep(BASE_TIME)
        elif (state is False) and (auto is True):
            self.__click_radio()
            time.sleep(BASE_TIME)
        self.__click_confirm()
        toast = self.__get_toast()
        time.sleep(BASE_TIME)
        if toast == "成功签署意见!":
            return True
        else:
            return False