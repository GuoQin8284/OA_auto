import time

from module.document_handle import DocumentHandle


class Send():
    def __init__(self,action):
        self.action = action
        self.documentHandle = DocumentHandle(action)
        self.send = "By.XPATH","//img[@title='送文']"
        self.all_frame = "By.XPATH", "//div[@class='layui-layer-content']/iframe"
        self.message = "By.XPATH","//div[contains(text(),'直接发送')]"
        self.confrim_btn = "By.XPATH","//a[contains(text(),'确定')]"
        self.cancel_btn = "By.XPATH","//a[contains(text(),'取消')]"
        self.wjbt = "By.ID","wjbt"

    # 获取提示消息
    def get_message(self):
        message =  self.action.find_element(self.message).text
        print("message:",message)
        return message

    def click_send_btn(self):
        self.action.find_element(self.send).click()

    def get_wjbt(self):
        return self.action.find_element(self.wjbt).text

    def send_text_flow(self,name):
        wjbt = self.get_wjbt()
        time.sleep(0.5)
        self.click_send_btn()
        time.sleep(0.5)
        self.action.driver.switch_to.frame(self.action.find_element(self.all_frame))
        time.sleep(0.5)
        if name in self.get_message():
            self.action.find_element(self.confrim_btn).click()
        else:
            self.action.find_element(self.cancel_btn).click()

        if (wjbt in self.documentHandle.get_document_titles()[0]) and (name in self.documentHandle.get_current_person()[0]):
            print("创建成功")
            return True
        else:
            print("创建失败")
            return False