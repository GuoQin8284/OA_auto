import time
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

    # 切换iframe到选择框
    def Switch_frame(self,ele):
        self.action.driver.switch_to.frame(self.action.find_element(ele))

    # 搜索部门或者人名，name可以传列表
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
        time.sleep(0.5)
        self.action.driver.switch_to.parent_frame()
        self.action.find_element(self.confirm).click()


    # 点击顶部的公司名称，是所有部门或这人员都展示在选择框内供选择
    def Click_company(self):
        self.action.find_element(self.company).click()

    # 选择要发送的部分或者人
    def Select_department_person(self):
        self.action.double_click(self.select_ele)


