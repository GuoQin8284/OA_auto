class DocumentHandle():
    def __init__(self,action):
        self.document_title = "By.XPATH","//td[@align='left']/a"
        self.current_person = "By.XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[8]"
        self.action = action

    def get_document_titles(self):
        eles = self.action.find_elements(self.document_title)
        titles = [x.text for x in eles]
        return titles

    def get_current_person(self):
        eles = self.action.find_elements(self.current_person)
        persons = [x.text for x in eles]
        return persons
