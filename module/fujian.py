import time

import allure
from selenium.webdriver.support.select import Select


class Fujian():

    def __init__(self,action):
        self.action = action

        # 附加按钮，点击进入附件页面
        self.fj_btn = "XPATH","//img[@title='附件']"
        # 上传附件按钮
        self.pull_fj_btn = "XPATH","//img[@alt='上传附件']"
        # 附件标题
        self.fj_title = "ID","bt"
        # 附件录入方式
        self.lrfs = "ID","lrfs"
        # 选择附件
        self.select_file = "ID","attach1"
        # 上传按钮
        self.upload_btn = "ID","btScfj"
        # 附件上传后的列表
        self.file_list = "XPATH","//tr[@align='left']/td[2]"
        # 保存按钮
        self.save_btn = "XPATH","//img[@title='保存']"
        # 关闭按钮
        self.close_btn = "XPATH","//img[@alt='关闭']"

    # 添加文件
    @allure.step(title="添加文件")
    def add_file(self,fileName):
        self.action.find_element(self.select_file).send_keys(fileName)
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 点击上传按钮上传文件
    @allure.step(title="点击上传按钮上传文件")
    def click_upload(self):
        self.action.find_element(self.upload_btn).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 选择文件录入方式
    @allure.step(title="选择文件录入方式")
    def select_lrfs(self,lrfs):
        Select(self.action.find_element(self.lrfs)).select_by_value(lrfs)
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 点击保存按钮
    @allure.step(title="点击保存按钮")
    def click_save(self):
        self.action.find_element(self.save_btn).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 获取alert弹窗的文本内容
    @allure.step(title="获取alert弹窗的文本内容")
    def get_alert_text(self):
        text = self.action.driver.switch_to.alert.text
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        return text

    # 点击alert弹窗的确认按钮，关闭弹窗
    @allure.step(title="点击alert弹窗的确认按钮，关闭弹窗")
    def accept_alert(self):
        self.action.driver.switch_to.alert.accept()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 关闭添加附件窗口
    @allure.step(title="关闭添加附件窗口")
    def close_window(self):
        self.action.find_element(self.close_btn).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 切换浏览器窗口到添加附件页面
    @allure.step(title="切换浏览器窗口到添加附件页面")
    def switch_window(self):
        window_list = self.action.driver.window_handles
        self.action.driver.switch_to.window(window_list[-1])

    # 上传文件业务流程
    @allure.step(title="上传文件业务流程")
    def fileUpload_folw(self,fileName):
        self.action.find_element(self.fj_btn).click()
        self.switch_window()
        self.action.find_element(self.pull_fj_btn).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        self.add_file(fileName)
        self.click_upload()
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)
        self.click_save()
        result_text = self.get_alert_text()
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)
        self.close_window()
        if "保存成功" in result_text:
            return True
        else:
            return False
