import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




class SelectPerson():
    def __init__(self,action):
        self.action = action
        # iframe大标签路径
        self.select_person = "By.XPATH",'//div[@class="layui-layer-content"]/iframe'
        # 中间输入框iframe
        self.ifmmiddle = "By.NAME",'ifmmiddle'
        # 公司路径
        self.company = "By.XPATH",'//span[@class="treetitle_1"]'
        # 搜索框
        self.searchName = "By.ID",'searchname'
        # 搜索按钮
        self.searchBtn = "By.XPATH",'//input[@value="搜索"]'
        # select选择框的id
        self.ojblist = "By.ID","objList"
        # 搜索到的元素
        self.select_ele = "By.XPATH","//select[@id='objList']/option"
        # 确认按钮
        self.confirm = "By.XPATH","//a[@class='btlink']/img"

        self.person_search_box = "ID","searchtext"  # 人员搜索输入框
        self.person_search_btn = "XPATH","//*[contains(text(),'搜索')]"  # 人员搜索按钮


    # 切换iframe到选择框
    @allure.step(title="切换iframe到选择框")
    def Switch_frame(self,ele):
        self.action.driver.switch_to.frame(self.action.find_element(ele))

    # 点击顶部的公司名称，是所有部门或这人员都展示在选择框内供选择
    @allure.step(title="点击顶部的公司名称，是所有部门或这人员都展示在选择框内供选择")
    def Click_company(self):
        self.action.find_element(self.company).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 选择要发送的部门或者人
    @allure.step(title="选择要发送的部门或者人")
    def Select_department_person(self):
        self.action.double_click(self.select_ele)
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)

    # 搜索部门或者人名，name可以传列表
    @allure.step(title="搜索部门 ")
    def SearchName(self,name):
        self.Switch_frame(self.select_person)
        self.Click_company()
        self.Switch_frame(self.ifmmiddle)
        if name:
            print("i",name)
            if type(name) is list:
                for i in name:
                    time.sleep(0.5)
                    self.action.find_element(self.searchName).clear()
                    time.sleep(0.5)
                    self.action.find_element(self.searchName).send_keys(i)
                    time.sleep(0.5)
                    self.action.find_element(self.searchBtn).click()
                    time.sleep(0.5)
                    self.Select_department_person()
            elif type(name) is str:
                time.sleep(0.5)
                self.action.find_element(self.searchName).clear()
                time.sleep(0.5)
                self.action.find_element(self.searchName).send_keys(name)
                time.sleep(0.5)
                self.action.find_element(self.searchBtn).click()
                time.sleep(0.5)
                self.Select_department_person()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(0.5)
        self.action.driver.switch_to.parent_frame()
        self.action.find_element(self.confirm).click()
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)



