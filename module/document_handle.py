import allure


class DocumentHandle():
    def __init__(self,action):
        self.document_title = "By.XPATH","//td[@align='left']/a"
        self.current_person = "By.XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[8]"
        self.action = action

    # 获取公文标题
    @allure.step(title="获取公文标题")
    def get_document_titles(self):
        eles = self.action.find_elements(self.document_title)
        titles = [x.text for x in eles]
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        return titles

    # 获取当前人员
    @allure.step(title="获取当前人员")
    def get_current_person(self):
        eles = self.action.find_elements(self.current_person)
        allure.attach(self.action.screen_shot(), "截图", allure.attachment_type.PNG)
        persons = [x.text for x in eles]
        return persons
