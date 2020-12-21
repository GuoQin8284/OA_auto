import logging
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from config import BASE_TIME
from driver.action import Action
from module.fujian import Fujian
from module.get_current_username import UserName
from module.read_opinion import ReadOpinion
from module.select_department import SelectDepartment
from module.send import Send
from page.menu import MenuFrame, Alert
from page.swgl.sw_cgx import SWCGXProxy
from page.swgl.swgl_yzj import SWYBJProxy


class SwcldPage(Action):
    def __init__(self, driver):
        super().__init__(driver)
        self.__swh = "ID", "selectlwfl"  # 收文号
        self.__lwdw = "ID", "lwdwmc"  # 来文单位
        self.__swrq = "ID", "swrq"  # 收文日期
        self.__jjcd = "ID", "jjcd"  # 紧急程度
        self.__fs = "ID", "fs"  # 份数
        self.__gwbh = "ID", "lwwh"  # 公文编号
        self.__blsx = "ID", "cb_blsx"  # 办理时限
        self.__cbsx = "ID", "cb_cbsx"  # 催办时限
        self.__wjbt = "ID", "wjbt"  # 公文标题
        self.__swlx = "ID", "swlx"  # 收文类型
        self.__ckzw = "ID", "filename__Fzwfj"  # 查看正文
        self.__zwsc_btn = "XPATH", "//img[@alt='上传']"  # 正文上传按钮
        self.__save_btn = "XPATH", "//img[@title='保存']"  # 保存按钮
        self.__readOpinion_btn = "XPATH", "//img[@title='阅文意见']"  # 阅文意见按钮
        self.__send_btn = "XPATH", "//img[@title='送文']"  # 发送按钮
        self.__fujian_btn = "XPATH", "//img[@title='附件']"  # 附件按钮
        self.__cldbt = "XPATH", "//center/font/font/b"  # 处理单标题
        self.__back = "XPATH", "//img[@title='返回']"  # 返回按钮
        self.__banjie = "XPATh", "//img[@title='办结']"  # 终结按钮
        self.menuFrame = MenuFrame(driver)
        self.alert = Alert(driver)

    #  点击办结
    def click_bj(self):
        self.click(self.__banjie)
        self.alert.alert_accept()

    # 获取处理单标题
    @allure.step(title="获取处理单标题")
    def get_cldbt(self):
        try:
            text = self.find_element(self.__cldbt).text
            allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
            return text
        except:
            return ""

    # 点击返回按钮
    @allure.step(title="点击返回按钮")
    def click_back(self):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.click(self.__back)

    # 点击保存按钮
    @allure.step(title="点击保存按钮")
    def click_save(self):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.click(self.__save_btn)
        alert = self.alert.get_alert_text()
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)
        if alert:
            return alert

    # 点击阅文意见按钮
    @allure.step(title="点击阅文意见按钮")
    def click_readOpinion(self):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.click(self.__readOpinion_btn)

    # 点击发送按钮
    @allure.step(title="点击发送按钮")
    def click_send(self):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.click(self.__send_btn)

    # 输入份数，num表示份数
    @allure.step(title="输入份数")
    def input_fs(self, num):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.input_text(self.__fs, num)

    # 选择紧急程度
    @allure.step(title="选择紧急程度")
    def select_jjcd(self, text):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        Select(self.find_element(self.__jjcd)).select_by_visible_text(text)

    # 输入收文日期
    def input_swrq(self,text):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.input_text(self.__swrq, text)

    # 输入标题
    @allure.step(title="输入发文标题")
    def input_bt_text(self, text):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.input_text(self.__wjbt, text)

    # 选择收文号
    def select_swh(self, swh):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        Select(self.find_element(self.__swh)).select_by_visible_text(swh)

    # 双击来文单位
    def doubleClick_lwdw(self):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        ActionChains(self.driver).double_click(self.find_element(self.__lwdw)).perform()

    # 进入选择来文单位窗口,选择来文单位
    def info_lwdw_window(self, lwdw, mc):
        lwfl = "ID", "m_DwflList"  # 来文分类选择框
        dwmc = "ID", "m_DwList"  # 单位名称
        fwz = "ID", 'm_FwzList'  # 发文字
        confrim_btn = "ID", "img_qd"  # 确认按钮
        cancl = "ID", "img_qx"  # 取消按钮
        lwdw_frame1 = "XPATH", "//div[@class='layui-layer-content']/iframe"  # 来文分类弹窗的iframe
        lwdw_frame2 = "ifsbody"
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_frame(self.find_element(lwdw_frame1))
        self.menuFrame.switch_frame(lwdw_frame2)
        Select(self.find_element(lwfl)).select_by_visible_text(lwdw)
        Select(self.find_element(dwmc)).select_by_visible_text(mc)
        self.menuFrame.switch_parent_iframe()
        self.click(confrim_btn)
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()

    # 输入来文编号
    def input_lwbg(self, gwbh):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.input_text(self.__gwbh, gwbh)

    # 输入办理时限
    def input_blsx(self, blsx):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.input_text(self.__blsx, blsx)

    # 输入催办时限
    def input_cbsx(self, cbsx):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.input_text(self.__cbsx, cbsx)

    # 选择收文类型
    def select_swlx(self, swlx):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        Select(self.find_element(self.__swlx)).select_by_visible_text(swlx)

    # 上传正文
    def sczw(self, filename):
        self.menuFrame.switch_default_content()
        self.menuFrame.switch_right_iframe()
        self.find_element(self.__ckzw).send_keys(filename)
        self.click(self.__zwsc_btn)


class SWCLDProxy(SwcldPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = UserName(driver)
        self.__search_department = SelectDepartment(driver)
        self.__readOpinion = ReadOpinion(driver)
        self.__send_flow = Send(driver)
        self.__fujian = Fujian(driver)
        self.__swcgx = SWCGXProxy(driver)
        self.__swybj = SWYBJProxy(driver)

    # 进入收文处理单页面
    @allure.step(title="进入收文处理单页面")
    def into_swcld(self):
        self.menuFrame.switch_default_content()
        self.contains_text("公文管理").click()  # 点击公文管理
        time.sleep(BASE_TIME)
        self.menuFrame.switch_left_iframe()
        self.contains_text("收文管理").click()  # 点击发文管理菜单
        time.sleep(BASE_TIME)
        self.contains_text("收文登记").click()  # 点击发文拟稿菜单，进入拟稿页面

    # 输入文章标题
    @allure.step(title="输入发文标题")
    def input_gwbt(self, text):
        time.sleep(BASE_TIME)
        self.input_bt_text(text)  # 输入公文标题

    # 发送流程（选择发文人发送）
    @allure.step(title="点击发送按钮，进入发送页面")
    def send_proxy(self, rec_name, lcname=None):
        self.click_send()
        time.sleep(BASE_TIME)
        self.__send_flow.send_text_flow(rec_name, lcname)

    # 保存发文
    @allure.step(title="保存发文")
    def save_document(self):
        return self.click_save()

    # 判断保存是否成功
    @allure.step(title="判断保存是否成功")
    def is_save_success(self, bt):
        get_ngr = self.__swcgx.get_ngr_list()[0]
        get_bt = self.__swcgx.get_wjbt_list()[0]
        # cur_user = self.username.get_username()
        if (get_ngr == self.username.get_username()) and (get_bt == bt):
            logging.info("保存成功")
            return True
        else:
            logging.info("保存失败")
            return False

    # 签署阅文意见
    def sign_readOpinion(self, readOpinion_text):
        self.click_readOpinion()
        return self.__readOpinion.signReadOpinion_proxy(readOpinion_text)

    # 添加附件
    def add_fujian(self, file):
        return self.__fujian.fileUpload_folw(file)

    # 选择来文单位
    def select_lwdw(self, lwdw, mc):
        self.doubleClick_lwdw()
        self.info_lwdw_window(lwdw, mc)

    # 填写处理单
    def input_swgl_info(self, swh="", lwdw=("", ""), swrq="", jjcd="", fs="",gwbh="",blsx="",cbsx="",gwbt="",swlx="",sczw=""):
        if swh != "":
            self.select_swh(swh)
            time.sleep(BASE_TIME)
        if "" not in lwdw:
            self.select_lwdw(lwdw[0], lwdw[1])
            time.sleep(BASE_TIME)
        if swrq != "":
            self.input_swrq(swrq)
            time.sleep(BASE_TIME)
        if jjcd != "":
            self.select_jjcd(jjcd)
            time.sleep(BASE_TIME)
        if fs != "":
            self.input_fs(fs)
            time.sleep(BASE_TIME)
        if gwbh != "":
            self.input_lwbg(gwbh)
            time.sleep(BASE_TIME)
        if blsx != "":
            self.input_blsx(blsx)
            time.sleep(BASE_TIME)
        if cbsx != "":
            self.input_cbsx(cbsx)
            time.sleep(BASE_TIME)
        if gwbt != "":
            self.input_gwbt(gwbt)
            time.sleep(BASE_TIME)
        if swlx != "":
            self.select_swlx(swlx)
            time.sleep(BASE_TIME)
        if sczw != "":
            # self.sczw(sczw)
            time.sleep(BASE_TIME)
        allure.attach(self.screen_shot(), "截图", allure.attachment_type.PNG)

    # 点击终结
    def end(self):
        self.click_bj()

    # 判断终结是否成功
    def is_end_success(self, bt):
        self.__swybj.into_Swbzl()
        bt_list = self.__swybj.get_wjbt_list()
        if bt in bt_list:
            return True
        else:
            return False

