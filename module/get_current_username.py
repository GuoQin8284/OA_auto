#!/usr/bin/python3
# -*- coding=utf-8 -*-
from driver.action import Action
from page.menu import MenuFrame


class UserName(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = MenuFrame(driver)
        self.username_ele = "ID", "username"

    # 获取当前登录账号的用户名
    def get_username(self):
        self.menu.switch_default_content()
        username = self.find_element(self.username_ele).text
        return username