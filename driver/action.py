import time
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
            print("element:",element)
            print("text:",text)
            self.find_element(element).send_keys(text)
        else:
            return False

    # 查找单个元素
    def find_element(self,location):
        def ananysis_element(ele):
            print("method_func:",ele)
            if ele == "By.ID":
                return By.ID
            elif ele == "By.CLASS_NAME":
                return By.CLASS_NAME
            elif ele == "By.CSS_SELECTOR":
                return By.CSS_SELECTOR
            elif ele == "By.LINK_TEXT":
                return By.LINK_TEXT
            elif ele == "By.NAME":
                return By.NAME
            elif ele == "By.TAG_NAME":
                return By.TAG_NAME
            elif ele == "By.XPATH":
                return By.XPATH
            elif ele == "By.PARTIAL_LINK_TEXT":
                return By.PARTIAL_LINK_TEXT
            else:
                raise "未解析的元素调用方法"


        if location:
            print("location[1]:",location)
            self.ele = WebDriverWait(self.driver,20,0.3).until(lambda x: x.find_element(ananysis_element(location[0]),location[1]))
            return self.ele
        else:
            return False

    # 查找一组元素
    def find_elements(self,location):
        def ananysis_element(ele):
            print("method_func:",ele)
            if ele == "By.ID":
                return By.ID
            elif ele == "By.CLASS_NAME":
                return By.CLASS_NAME
            elif ele == "By.CSS_SELECTOR":
                return By.CSS_SELECTOR
            elif ele == "By.LINK_TEXT":
                return By.LINK_TEXT
            elif ele == "By.NAME":
                return By.NAME
            elif ele == "By.TAG_NAME":
                return By.TAG_NAME
            elif ele == "By.XPATH":
                return By.XPATH
            elif ele == "By.PARTIAL_LINK_TEXT":
                return By.PARTIAL_LINK_TEXT
            else:
                raise "未解析的元素调用方法"


        if location:
            print("location[1]:",location)
            self.eles = WebDriverWait(self.driver,20,0.3).until(lambda x: x.find_elements(ananysis_element(location[0]),location[1]))
            return self.eles
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
