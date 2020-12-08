from driver.action import Action


class MenuFrame(Action):

    def __init__(self,driver):
        super().__init__(driver)
        self.doc_manager = "公文管理"  # 公文管理元素
        self.left_iframe = "left"  # 左边菜单iframe
        self.right_iframe = "rfm"  # 右边内容框iframe


    def switch_left_iframe(self):
        self.driver.switch_to.frame(self.left_iframe)

    def switch_right_iframe(self):
        print(self.right_iframe)
        self.driver.switch_to.frame(self.right_iframe)

    def switch_parent_iframe(self):
        self.driver.switch_to.parent_frame()

    def switch_default_content(self):
        self.driver.switch_to.default_content()