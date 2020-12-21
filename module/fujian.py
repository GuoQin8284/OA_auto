import allure
from selenium.webdriver.support.select import Select
from driver.action import Action
from page.menu import MenuFrame, Alert


class Fujian:

    def __init__(self, driver):
        self.__action = Action(driver)
        self.__menuFrame = MenuFrame(driver)
        self.__alert = Alert(driver)
        # 附加按钮，点击进入附件页面
        self.__fj_btn = "XPATH", "//img[@title='附件']"
        # 上传附件按钮
        self.__pull_fj_btn = "XPATH", "//img[@alt='上传附件']"
        # 附件标题
        self.__fj_title = "ID", "bt"
        # 附件录入方式
        self.__lrfs = "ID", "lrfs"
        # 选择附件
        self.__select_file = "ID", "attach1"
        # 上传按钮
        self.__upload_btn = "ID", "btScfj"
        # 起草附件按钮
        self.__qc_btn = "XPATh", "//img[@alt='起草附件']"
        # 起草标题输入框
        self.__qc_input_box = "ID", "bt"
        # 附件上传后的列表
        self.__file_list = "XPATH", "//tr[@align='left']/td[2]"
        # 保存按钮
        self.__save_btn = "XPATH", "//img[@title='保存']"
        # 关闭按钮
        self.__close_btn = "XPATH", "//img[@alt='关闭']"

    # 添加文件
    @allure.step(title="添加文件")
    def __add_file(self, fileName):
        self.__action.find_element(self.__select_file).send_keys(r"{}".format(fileName))
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 点击上传按钮上传文件
    @allure.step(title="点击上传按钮上传文件")
    def __click_upload(self):
        self.__action.find_element(self.__upload_btn).click()
        self.__alert.alert_accept()
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 选择文件录入方式
    @allure.step(title="选择文件录入方式")
    def __select_lrfs(self,lrfs):
        Select(self.__action.find_element(self.__lrfs)).select_by_value(lrfs)
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 点击保存按钮
    @allure.step(title="点击保存按钮")
    def __click_save(self):
        self.__action.find_element(self.__save_btn).click()
        text = self.__alert.get_alert_text()
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        return text

    # 关闭添加附件窗口
    @allure.step(title="关闭添加附件窗口")
    def __close_window(self):
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        self.__action.find_element(self.__close_btn).click()

    # 切换浏览器窗口到添加附件页面
    @allure.step(title="切换浏览器窗口到添加附件页面")
    def __switch_window(self):
        window_list = self.__action.driver.window_handles
        self.__action.driver.switch_to.window(window_list[-1])

    # 上传文件业务流程
    @allure.step(title="上传文件业务流程")
    def fileUpload_folw(self, fileName):
        self.__menuFrame.switch_default_content()
        self.__menuFrame.switch_right_iframe()
        self.__action.find_element(self.__fj_btn).click()
        self.__switch_window()
        self.__action.find_element(self.__pull_fj_btn).click()
        self.__add_file(fileName)
        allure.attach(self.__action.screen_shot(), "截图", allure.attachment_type.PNG)
        self.__click_upload()
        result_text = self.__click_save()
        self.__close_window()
        self.__switch_window()
        if "保存成功" in result_text:
            return True
        else:
            return False
