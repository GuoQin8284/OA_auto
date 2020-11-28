import allure

from driver.action import Action


class Verify_code():

    def __init__(self,action):
        self.action = action
        self.verfiy_input = "XPATH","//input[@placeholder='验证码']"

    #判断验证码输入框是否存在
    @allure.step(title="判断验证码输入框是否存在")
    def get_verify_status(self):
        if self.action.find_element(self.verfiy_input,timeout=1,poll_frequency=0.1):
            allure.attach(self.action.screen_shot(),"截图",allure.attachment_type.PNG)
            return True
        else:
            return False

    def input_verify_code(self):
        self.action.input_text(self.verfiy_input,input("请输入验证码："))
        allure.attach(self.action.screen_shot(),"截图",allure.attachment_type.PNG)

    def verify_code_flow(self):
        if self.get_verify_status():
            self.input_verify_code()
        else:
            return False

