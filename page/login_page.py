from driver.action import Action
from page.menu import MenuFrame


class LoginPage(Action):

    def __init__(self,driver):
        super().__init__(driver)
        self.menuFrame = MenuFrame(driver)
        self.username_ele = "ID", "userid"
        self.pwd_ele = "ID", "pwd"
        self.login_btn_ele = "ID", "loginimage"
        self.verfiy_input = "XPATH", "//input[@placeholder='验证码']"
        self.login_err_toast_ele = "ID", "reasontext"
        self.login_success_toast_ele = "当前用户"
        self.logout_btn_ele = "XPATH", "//a[@title='退出登录']"

    # 输入用户名
    def input_username(self,username):
        self.input_text(self.username_ele,username)

    # 输入密码
    def input_pwd(self,pwd):
        self.input_text(self.pwd_ele,pwd)

    # 判断验证码输入框是否存在
    def get_verify_status(self):
        if self.find_element(self.verfiy_input, timeout=1, poll_frequency=0.1):
            return True
        else:
            return False

    # 输入验证码
    def input_verify_code(self):
        self.input_text(self.verfiy_input, input("请输入验证码："))

    # 点击登录按钮
    def click_login_btn(self):
        self.click(self.login_btn_ele)

    # 获取登录失败时的提示信息
    def get_login_err_toast(self):
        element = self.find_element(self.login_err_toast_ele,timeout=2)
        if element:
            return element.text
        else:
            return False

    # 获取登录成功时的标志信息
    def get_login_success_toast(self):
        element =  self.contains_text(self.login_success_toast_ele,timeout=2)
        if element:
            return element.text
        else:
            return False

    # 点击退出登录按钮
    def click_logout_btn(self):
        self.click(self.logout_btn_ele)


# 业务类
class LoginProxy(LoginPage):

    # 登录业务，输入用户名、密码、验证码
    def Login(self, username=None, pwd=None):
        self.input_username(username)
        self.input_pwd(pwd)
        if self.get_verify_status():
            self.input_verify_code()
        self.click_login_btn()

    # 登录状态检测
    def get_login_status(self):
        self.err = ""
        self.success = ""
        self.err = self.get_login_err_toast()
        self.success = self.get_login_success_toast()
        print("err:", self.err)
        print("success:", self.success)
        if self.success:
            return self.success
        else:
            return self.err

    # 点击退出登录按钮，退出登录
    def Logout(self):
        self.menuFrame.switch_default_content()
        self.click_logout_btn()

    # 切换登录用户
    def switch_loginUser(self, username=None, pwd=None):
        self.Logout()
        self.Login(username, pwd)
