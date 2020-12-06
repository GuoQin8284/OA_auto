import time
from selenium import webdriver

from script import Test_demo01

driver = webdriver.Ie()
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8092/fwgl/frmfwcld.jsp")
driver.switch_to.default_content()
# driver.find_element_by_name("userid").send_keys("hcadmin")
# driver.find_element_by_name("pwd").send_keys("123456")
# driver.find_element_by_id("loginimage").click()
#
# driver.find_element_by_xpath("//img[@title='附件']").click()
# cur = driver.current_window_handle
# all = driver.window_handles
# print("cur:",cur)
# print("all:",all)
# driver.switch_to.window(all[-1])
# driver.find_element_by_xpath("//img[@alt='上传附件']").click()
# all = driver.window_handles
# print("cur:",cur)
# print("all:",all)
# driver.switch_to.window(all[-1])
# driver.find_element_by_id("attach1").send_keys(r"E:\gq_郭钦\程序包文件\合同管理\配置语句.txt")
# driver.find_element_by_xpath("//input[@value='上传']").click()


a = ["1","2"]

if type(a) is list:
    print(True)