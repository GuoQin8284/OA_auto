import time

import allure

from config import BASE_TIME


class ReadOpinion():
    def __init__(self,action):
        # 第一层frame
        self.all_frame = "By.XPATH","//div[@class='layui-layer-content']/iframe"
        # 阅文意见输入框
        self.content = "By.ID","TextContent"
        # 确认后打开送文框的单选框
        self.Radio = "By.ID","autoLoadSendDlg"
        # 确认按钮
        self.confirm = "By.ID","img_qd"
        # 初始化action类
        self.action = action
        # 修改成功的toast提示
        self.toast = "By.XPATH",'//div[contains(text(),"成功签署意见!")]'

    # 输入阅文意见
    @allure.step(title="输入阅文意见")
    def input_content(self,text):
        self.action.find_element(self.content).send_keys(text)
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 获取送文单选框的状态
    @allure.step(title="获取送文单选框的状态")
    def get_radio_state(self):
        state = self.action.find_element(self.Radio).is_selected()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        return state

    # 点击送文单选框
    @allure.step("点击送文单选框")
    def click_radio(self):
        self.action.find_element(self.Radio).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 点击确认按钮
    @allure.step(title="点击确认按钮")
    def click_confirm(self):
        self.action.find_element(self.confirm).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 获取阅文意见签约成功的toast
    @allure.step(title="获取阅文意见签约成功的toast")
    def get_toast(self):
        toast = self.action.find_element(self.toast).text
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        return toast
    # 输入阅文意见的业务流程
    @allure.step(title="阅文意见的业务流程")
    def input_content_flow_path(self,text):
        self.action.driver.switch_to.frame(self.action.find_element(self.all_frame))
        time.sleep(BASE_TIME)
        self.input_content(text)
        time.sleep(BASE_TIME)
        state = self.get_radio_state()
        if state:
            self.click_radio()
            time.sleep(BASE_TIME)
        self.click_confirm()
        toast = self.get_toast()
        if toast == "成功签署意见!":
            return True
        else:
            return False