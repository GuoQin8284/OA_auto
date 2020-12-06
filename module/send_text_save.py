
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
    def save_text_flow(self,url,bt_text):  # 这是发文保存的业务流程
        self.action.get_url(url)  # 获取driver对象
        self.action.input_text(self.bt,bt_text)  # 输入标题
        self.action.click(self.save_btn)  # 点击保存按钮
        try:
            result = self.action.contains_text(bt_text)  # 搜索列表中是否包含标题文字，如果包含则将列表中文字返回
            allure.attach(self.action.screen_shot(),"截图",allure.attachment_type.PNG)  # 截图
            return result
        except:
            allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)  # 如果不包含，则返回False
            return "未找到元素"