import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from driver.log_method import log_method


class Action:

    def __init__(self, driver):
        self.driver = driver

    # 元素定位方法解析
    def __ananysis_element(self, ele):
        if ele in ("By.ID", "ID"):
            return By.ID
        elif ele in ("By.CLASS_NAME", "CLASS_NAME"):
            return By.CLASS_NAME
        elif ele in ("By.CSS_SELECTOR", "CSS"):
            return By.CSS_SELECTOR
        elif ele in ("By.LINK_TEXT", "LINK_TEXT"):
            return By.LINK_TEXT
        elif ele in ("By.NAME", "NAME"):
            return By.NAME
        elif ele in ("By.TAG_NAME", "TAG_NAME"):
            return By.TAG_NAME
        elif ele in ("By.XPATH", "XPATH"):
            return By.XPATH
        elif ele in ("By.PARTIAL_LINK_TEXT", "PARTIAL"):
            return By.PARTIAL_LINK_TEXT
        else:
            return "未解析的元素调用方法"

    # 输入文字
    def input_text(self, element, text):
        if text and element:
            # print("element:",element)
            # print("text:",text)
            self.find_element(element).clear()
            self.find_element(element).send_keys(text)
        else:
            return False

    # 查找单个元素
    def find_element(self, location, timeout=3, poll_frequency=0.1):
        if location:
            # print("location[1]:",location)
            try:
                ele = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(self.__ananysis_element(location[0]), location[1]))
                return ele
            except TimeoutException:
                return False
        else:
            return False

    # 查找一组元素
    def find_elements(self, location, timeout=3, poll_frequency=0.1):
        if location:
            # print("location[1]:", location)
            try:
                ele = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(self.__ananysis_element(location[0]), location[1]))
                return ele
            except TimeoutException:
                # print(r"未找到{}元素".format(location[1]))
                return False
        else:
            return False

    # 点击元素
    def click(self, element):
        if element:
            self.find_element(element).click()
        else:
            return False

    # 双击元素
    def double_click(self, element):
        if element:
            # print("element:", element)
            # ele = self.find_element(element).click()
            # print("点击第一下")
            # time.sleep(0.1)
            # self.find_element(element).click()
            # print("点击第二下")
            ele = self.find_element(element)
            ActionChains(self.driver).double_click(ele).perform()
        else:
            return False

    # 清空输入
    def clean_text(self, element):
        if element:
            self.find_element(element).send_keys(Keys.CONTROL,"a")
            self.find_element(element).send_keys(Keys.BACKSPACE)
        else:
            return False

    # 根据文本模糊定位
    def contains_text(self, text1, timeout=2):
        if text1:
            element = "By.XPATH", "//*[contains(text(),'{}')]".format(text1)
            print("element:",element)
            ele = self.find_element(element, timeout)
            return ele

    def screen_shot(self):
        return self.driver.get_screenshot_as_png()

    # 打开指定的网址
    def get_url(self, url):
        self.driver.get(url)
