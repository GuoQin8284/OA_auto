
# 发文保存流程
import allure



class SendTextSave():

    def __init__(self,action):
        # 初始化action对象
        self.action = action
        # 保存按钮元素
        self.save_btn = "By.XPATH","//img[@title='保存']"
        self.bt = "By.ID","wjbt"

    @allure.step(title="发文保存保存流程")
    def save_text_flow(self,url,bt_text):
        self.action.get_url(url)
        self.action.input_text(self.bt,bt_text)
        self.action.click(self.save_btn)
        try:
            result = self.action.contains_text(bt_text)
            allure.attach(self.action.screen_shot(),"截图",allure.attachment_type.PNG)
            return result
        except:
            allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
            return "未找到定位"