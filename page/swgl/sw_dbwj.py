#!/usr/bin/python3
# -*- coding=utf-8 -*-
import logging
import time

import allure

from config import BASE_TIME
from driver.action import Action
from page.menu import Alert, MenuFrame


class SwdbPage(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.__MenuFrame = MenuFrame(driver)
        self.__alert = Alert(driver)
        self.__rows = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]"
        self.__select_box = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>{}]/td[1]"  # 选择框
        self.__swrq_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[2]"  # 收文日期
        self.__swh_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[3]"  # 收文号
        self.__lwdw_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[4]"  # 来文单位
        self.__lwwh_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[5]"  # 来文文号
        self.__wjbt_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[6]"  # 文件标题
        self.__zbbm_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[7]"  # 主办部门
        self.__currentHandlePerosn_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[8]"  # 当前办理人
        self.__blsx_list = "XPATH", "//div[@class='maincontent']/table/tbody/tr[position()>1]/td[9]"  # 办理时限
        self.__delete_btn = "XPATH", "//img[@alt='删除']"
        self.__selectAll = "XPATH", "//span[@class='qx_first']/input"
        self.__timeout = 2

    # 获取文件标题列表
    @allure.step(title="获取文件标题列表")
    def get_wjbt_list(self):
        eles = self.find_elements(self.__wjbt_list, timeout=self.__timeout)
        if len(eles) > 0:
            wjbt_list = [x.text.strip() for x in eles]
            return wjbt_list

    # 获取收文日期列表
    @allure.step(title="获取收文日期列表")
    def get_swrq_list(self):
        eles = self.find_elements(self.__swrq_list, timeout=self.__timeout)
        if len(eles) > 0:
            swrq_list = [x.text.strip() for x in eles]
            return swrq_list

    # 获取收文号列表
    @allure.step(title="获取收文号列表")
    def get_swh_list(self):
        eles = self.find_elements(self.__swh_list, timeout=self.__timeout)
        if len(eles) > 0:
            swh_list = [x.text.strip() for x in eles]
            return swh_list

    # 获取来文单位列表
    @allure.step(title="获取来文单位列表")
    def get_lwdw_list(self):
        eles = self.find_elements(self.__lwdw_list, timeout=self.__timeout)
        if len(eles) > 0:
            lwdw_list = [x.text.strip() for x in eles]
            return lwdw_list

    # 获取来文文号列表
    @allure.step(title="获取来文文号列表")
    def get_lwwh_list(self):
        eles = self.find_elements(self.__lwwh_list,timeout=self.__timeout)
        if len(eles) > 0:
            lwwh_list = [x.text.strip() for x in eles]
            return lwwh_list

    # 按行的方式获取整行的元素列表，返回的是一个包含所有行元素的列表
    @allure.step(title="按行的方式获取整行的元素列")
    def get_rows_list(self):
        try:
            eles = self.find_elements(self.__rows, timeout=self.__timeout)
            return eles
        except:
            return []

    # 根据公文索引删除公文
    @allure.step(title="根据公文索引删除公文")
    def ByDeleteIndex(self, index):
        if isinstance(index, int):
            ele1 = self.__select_box[0], self.__select_box[1].format(index + 1)
            self.click(ele1)
            self.click(self.__delete_btn)
            self.__alert.alert_accept()
        elif isinstance(index, list) and len(index) > 0:
            for i in index:
                ele2 = self.__select_box[0], self.__select_box[1].format(i + 1)
                self.click(ele2)
                time.sleep(0.05)
            time.sleep(BASE_TIME)
            self.click(self.__delete_btn)
            time.sleep(BASE_TIME)
            self.__alert.alert_accept()

    # 点击全选
    @allure.step(title="点击草稿箱全选按钮")
    def click_selectAll(self):
        self.click(self.__selectAll)

    # 根据标题获取该公文在草稿箱中的索引位置
    @allure.step(title="根据标题获取该标题在办理中列表的索引位置")
    def getByBtIndex(self, bt):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        eles = self.get_rows_list()
        if eles:
            ele_index = [eles.index(x) for x in eles if bt in x.text.strip()]
            return ele_index
        else:
            return []

    # 根据标题获取该公文的相关信息
    @allure.step(title="根据标题获取该公文的相关信息")
    def getByBtInfo(self, bt):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        eles = self.get_rows_list()
        if eles:
            btInfo = [x.text for x in eles if bt in x.text.strip()]
            return btInfo
        else:
            return []

    # 获取当前页面当前办理人列表
    @allure.step(title="获取当前页面当前办理人列表")
    def get_CurrentHandlePerson_list(self):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        try:
            eles = self.find_elements(self.__currentHandlePerosn_list, self.__timeout)
            person_list = [x.text.strip() for x in eles]
            return person_list
        except:
            return []

    # 获取主办部门列表
    @allure.step(title="获取主办部门列表")
    def get_zbbm_list(self):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        try:
            eles = self.find_elements(self.__zbbm_list, timeout=self.__timeout)
            zbbm_list = [x.text.strip() for x in eles]
            return zbbm_list
        except:
            return []

    # 获取办理时限列表
    @allure.step(title="获取办理时限列表")
    def get_blsx_list(self):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        try:
            eles = self.find_elements(self.__blsx_list, timeout=self.__timeout)
            blsx_list = [x.text.strip() for x in eles]
            return blsx_list
        except:
            return []


class SWDBProxy(SwdbPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__MenuFrame = MenuFrame(driver)

    # 进入收文待办页面
    @allure.step(title="进入收文待办页面")
    def into_Swbzl(self):
        self.__MenuFrame.switch_default_content()
        self.contains_text("公文管理").click()  # 点击公文管理
        time.sleep(BASE_TIME)
        self.__MenuFrame.switch_left_iframe()
        self.contains_text("收文管理").click()  # 点击收文管理菜单
        time.sleep(BASE_TIME)
        self.contains_text("待办文件").click()

    # 根据发文标题，进入处理单页面
    @allure.step(title="根据收文标题，进入处理单页面")
    def into_doc(self, bt):
        self.__MenuFrame.switch_default_content()
        self.__MenuFrame.switch_right_iframe()
        try:
            self.contains_text(bt, timeout=2).click()
        except AttributeError:
            logging.info("\'{}\'".format(bt) + "公文不存在!")
            pass

    # 根据收文标题，删除办理中的收文
    @allure.step(title="根据收文标题，删除办理中列表的发文")
    def delete_doc(self, bt):
        ele_index = self.getByBtIndex(bt)
        self.ByDeleteIndex(ele_index)

    # 判断删除是否成功
    @allure.step("判断删除是否成功")
    def is_delete_success(self, bt):
        if self.getByBtInfo(bt):  # 如果返回为不为空，表明公文未删除，则返回Flase
            return False
        else:  # 如果返回为为空，表明公文已删除，则返回True
            return True

    # 根据标题获取收文文号
    @allure.step(title="根据标题获取收文文号")
    def getByDocSwwh(self, bt):
        index = self.getByBtIndex(bt)
        if index:
            fwwg_list = [self.get_swh_list()[x] for x in index]
            return fwwg_list
        else:
            return []

    # 根据标题获取收文日期
    @allure.step(title="根据标题获取收文文号")
    def getByDocSwwh(self, bt):
        index = self.getByBtIndex(bt)
        if index:
            fwwg_list = [self.get_swrq_list()[x] for x in index]
            return fwwg_list
        else:
            return []

    # 根据标题获取当前办理人
    @allure.step(title="根据标题获取当前办理人")
    def getByDocCurrentPerson(self, bt):
        index = self.getByBtIndex(bt)
        if index:
            person_list = [self.get_CurrentHandlePerson_list()[x] for x in index]
            return person_list
        else:
            return []