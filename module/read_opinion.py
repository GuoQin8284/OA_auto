import time


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
    def input_content(self,text):
        self.action.find_element(self.content).send_keys(text)

    # 获取送文单选框的状态
    def get_radio_state(self):
        return self.action.find_element(self.Radio).is_selected()

    # 点击送文单选框
    def click_radio(self):
        self.action.find_element(self.Radio).click()

    # 点击确认按钮
    def click_confirm(self):
        self.action.find_element(self.confirm).click()

    def get_toast(self):
        return self.action.find_element(self.toast).text

    # 输入阅文意见的业务流程
    def input_content_flow_path(self,text):
        self.action.driver.switch_to.frame(self.action.find_element(self.all_frame))
        time.sleep(1)
        self.input_content(text)
        time.sleep(1)
        state = self.get_radio_state()
        if state:
            self.click_radio()
            time.sleep(1)
        self.click_confirm()
        toast = self.get_toast()
        if toast == "成功签署意见!":
            return True
        else:
            return False