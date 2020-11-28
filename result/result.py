import allure


@allure.step(title="获取alert弹窗的文本内容")
def get_alert_text(self):
    text = self.action.driver.switch_to.alert.text
    allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
    return text

@allure.step(title="返回指定的元素文本值")
def contains_text(self, text1):
    if text1:
        element = "By.XPATH", "//*[contains(text(),'{}')]".format(text1)
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        print("element:", element)
        try:
            text = self.find_element(element).text
            print("text:", text)
            return text
        except Exception:
            return False
