import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait



class Action ():

    def __init__(self,driver):
        self.driver = driver
        self.actionchains = ActionChains(self.driver)

    # 输入文字
    def input_text(self,element,text):
        if text and element:
            # print("element:",element)
            # print("text:",text)
            self.find_element(element).send_keys(text)
        else:
            return False

    # 查找单个元素
    def find_element(self,location):
        def ananysis_element(ele):
            if ele in ("By.ID","ID") :
                return By.ID
            elif ele in ("By.CLASS_NAME","CLASS_NAME"):
                return By.CLASS_NAME
            elif ele in ("By.CSS_SELECTOR","CSS"):
                return By.CSS_SELECTOR
            elif ele in ("By.LINK_TEXT","LINK_TEXT"):
                return By.LINK_TEXT
            elif ele in ("By.NAME","NAME"):
                return By.NAME
            elif ele in ("By.TAG_NAME","TAG_NAME"):
                return By.TAG_NAME
            elif ele in ("By.XPATH","XPATH"):
                return By.XPATH
            elif ele in ("By.PARTIAL_LINK_TEXT","PARTIAL"):
                return By.PARTIAL_LINK_TEXT
            else:
                raise print("未解析的元素调用方法")


        if location:
            # print("location[1]:",location)
            try:
                self.ele = WebDriverWait(self.driver,20,0.3).until(lambda x: x.find_element(ananysis_element(location[0]),location[1]))
                return self.ele
            except TimeoutException as f :
                raise print(r"未找到{}元素".format(location[1]))

        else:
            return False

    # 查找一组元素
    def find_elements(self,location):
        def ananysis_element(ele):
            if ele in ("By.ID","ID") :
                return By.ID
            elif ele in ("By.CLASS_NAME","CLASS_NAME"):
                return By.CLASS_NAME
            elif ele in ("By.CSS_SELECTOR","CSS"):
                return By.CSS_SELECTOR
            elif ele in ("By.LINK_TEXT","LINK_TEXT"):
                return By.LINK_TEXT
            elif ele in ("By.NAME","NAME"):
                return By.NAME
            elif ele in ("By.TAG_NAME","TAG_NAME"):
                return By.TAG_NAME
            elif ele in ("By.XPATH","XPATH"):
                return By.XPATH
            elif ele in ("By.PARTIAL_LINK_TEXT","PARTIAL"):
                return By.PARTIAL_LINK_TEXT
            else:
                raise print("未解析的元素调用方法")


        if location:
            # print("location[1]:", location)
            try:
                self.ele = WebDriverWait(self.driver,20,0.3).until(lambda x: x.find_elements(ananysis_element(location[0]),location[1]))
                return self.ele
            except TimeoutException as f :
                raise print(r"未找到{}元素".format(location[1]))
        else:
            return False

    # 点击元素
    def click(self,element):
        if element:
            self.find_element(element).click()
        else:
            return False

    # 双击元素
    def double_click(self,element):
        if element:
            self.actionchains.double_click(self.find_element(element)).perform()
        else:
            return False

    # 清空输入
    def clean_text(self,element):
        if element:
            self.find_element(element).send_keys(Keys.CONTROL,"a")
            self.find_element(element).send_keys(Keys.BACKSPACE)
        else:
            return False

    def contains_text(self,text1):
        if text1:
            element = "By.XPATH","//*[contains(text(),'{}')]".format(text1)
            print("element:",element)
            try:
                text =self.find_element(element).text
                print("text:",text)
                return text
            except Exception:
                return False

    def select_group(self,*select):
        ele = "By.XPATH","//a[@class='treetitletext_0' and @p1='treetitletext']"
