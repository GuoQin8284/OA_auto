import logging
import time

import allure

from config import BASE_TIME
from driver.action import Action


# 选择部门
class SelectDepartment(Action):
    def __init__(self,driver):
        super().__init__(driver)
        # iframe大标签路径
        self.select_department = "By.XPATH",'//div[@class="layui-layer-content"]/iframe'
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

        # self.person_search_box = "ID","searchtext"  # 人员搜索输入框
        # self.person_search_btn = "XPATH","//*[contains(text(),'搜索')]"  # 人员搜索按钮


    # 切换iframe到选择框
    @allure.step(title="切换iframe到选择框")
    def Switch_frame(self,ele):
        self.driver.switch_to.frame(self.find_element(ele))

    # 点击顶部的公司名称，是所有部门都展示在选择框内供选择
    @allure.step(title="点击顶部的公司名称，是所有部门或这人员都展示在选择框内供选择")
    def Click_company(self):
        self.find_element(self.company).click()
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)

    # 选择要发送的部门
    @allure.step(title="选择要发送的部门")
    def Select_department(self):
        self.double_click(self.select_ele)
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)

    # 搜索输入的部门，并选择，name可以传列表
    @allure.step(title="搜索部门 ")
    def SearchName(self,name):
        self.Switch_frame(self.select_department)
        logging.info("切换iframe到{}".format(self.select_department))
        self.Click_company()
        logging.info("点击公司名称")
        self.Switch_frame(self.ifmmiddle)
        logging.info("切换iframe到{}".format(self.ifmmiddle))
        if name:
            logging.info("name不为空，继续下面操作，name：{}".format(name))
            if type(name) is list:
                logging.info("name为一个list，继续下面操作，name：{}".format(name))
                for i in name:
                    time.sleep(BASE_TIME)
                    self.find_element(self.searchName).clear()
                    logging.info("清空搜索框")
                    time.sleep(BASE_TIME)
                    self.find_element(self.searchName).send_keys(i)
                    logging.info("输入部门关键词，关键词：{}".format(i))
                    time.sleep(BASE_TIME)
                    self.find_element(self.searchBtn).click()
                    logging.info("点击搜索按钮")
                    time.sleep(BASE_TIME)
                    self.Select_department()
                    logging.info("调用Select_department函数，选择搜索结果")
            elif type(name) is str:
                logging.info("name为一个字符串，继续下面操作，name：{}".format(name))
                time.sleep(BASE_TIME)
                self.find_element(self.searchName).clear()
                logging.info("清空搜索框")
                time.sleep(BASE_TIME)
                self.find_element(self.searchName).send_keys(name)
                logging.info("输入部门关键词，关键词：{}".format(name))
                time.sleep(BASE_TIME)
                self.find_element(self.searchBtn).click()
                logging.info("点击搜索按钮")
                time.sleep(BASE_TIME)
                self.Select_department()
                logging.info("调用Select_department函数，选择搜索结果")
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        time.sleep(BASE_TIME)
        self.driver.switch_to.parent_frame()
        logging.info("切回到上一层iframe")
        self.find_element(self.confirm).click()
        logging.info("点击确认按钮，关闭弹窗")
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)