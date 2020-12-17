#!/usr/bin/python3
# -*- coding=utf-8 -*-
import time

from config import BASE_TIME
from driver.action import Action
from page.menu import Alert, MenuFrame


class fwcgxPage(Action):

    def __init__(self,driver):
        super().__init__(driver)
        self.__alert = Alert(driver)
        self.__rows = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]"
        self.__ngr = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[4]"
        self.__wjbt_list = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[5]"
        self.__ngdw_list = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[3]"
        self.__ngrq_list = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[2]"
        self.__fwlx_list = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[6]"
        self.__fwwh_list = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>1]/td[7]"
        self.__delete_btn = "XPATH","//img[@alt='删除']"
        self.__selectAll = "XPATH","//span[@class='qx_first']/input"


    # 获取文件标题列表
    def get_wjbt_list(self):
        eles = self.find_elements(self.__wjbt_list)
        if len(eles) > 0:
            wjbt_list = [x.text.strip() for x in eles]
            return wjbt_list

    # 获取单位列表
    def get_ngdw_list(self):
        eles = self.find_elements(self.__ngdw_list)
        if len(eles) > 0:
            ngdw_list = [x.text.strip() for x in eles]
            return ngdw_list

    # 获取拟稿日期列表
    def get_ngrq_list(self):
        eles = self.find_elements(self.__ngrq_list)
        if len(eles) > 0:
            ngrq_list = [x.text.strip() for x in eles]
            return ngrq_list

    # 获取发文类型列表
    def get_fwlx_list(self):
        eles = self.find_elements(self.__fwlx_list)
        if len(eles) > 0:
            fwlx_list = [x.text.strip() for x in eles]
            return fwlx_list

    # 获取发文文号列表
    def get_fwwh_list(self):
        eles = self.find_elements(self.__fwwh_list)
        if len(eles) > 0:
            fwwh_list = [x.text.strip() for x in eles]
            return fwwh_list

    # 获取拟稿人列表
    def get_ngr_list(self):
        eles = self.find_elements(self.__ngr)
        if len(eles) > 0:
            ngr_list = [x.text.strip() for x in eles]
            return ngr_list

    # 按行的方式获取整行的元素列表，返回的是一个包含所有行元素的列表
    def get_rows_list(self):
        eles = self.find_elements(self.__rows)
        return eles

    # 删除草稿箱
    def delete(self,num):
        if isinstance(num,int):
            self.ele =  "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>{}]/td[1]".format(num+1)
            self.click(self.ele)
            self.click(self.__delete_btn)
            self.__alert.alert_accept()
        elif isinstance(num,list) and len(num)> 0:
            for i in num:
                self.ele = "XPATH","//div[@class='maincontent']/table/tbody/tr[position()>{}]/td[1]".format(i+1)
                self.click(self.ele)
            self.click(self.__delete_btn)
            self.__alert.alert_accept()
    # 点击全选
    def click_selectAll(self):
        self.click(self.__selectAll)

    def delete_rowsEle(self,ele):
        if isinstance(ele,list):
            for i in ele:
                self.click(i[0])


class CGX_proxy(fwcgxPage):
    def __init__(self,driver):
        super().__init__(driver)
        self.__MenuFrame = MenuFrame(driver)
    def into_fwcgx(self):
        self.contains_text("公文管理").click()  # 点击公文管理
        time.sleep(BASE_TIME)
        self.__MenuFrame.switch_left_iframe()
        self.contains_text("发文管理").click()  # 点击发文管理菜单
        time.sleep(BASE_TIME)
        self.contains_text("草 稿 箱").click()

    def into_doc(self,bt):
        self.contains_text(bt).click()

    def delete_doc(self,bt):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        ele = self.get_rows_list()
        text_list = [ele.index(x) for x in ele if bt in x.text]
