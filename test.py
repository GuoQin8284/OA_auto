import time

import os
from selenium import webdriver


# driver = webdriver.Ie()
# from page.menu import Alert
#
# driver = webdriver.Chrome()
#
# driver.get("http:www.baidu.com")
# Alert(driver).get_alert_text()
# driver.switch_to.default_content()
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


# a = ["1"]
#
# if type(a) is list:
#     print(True)
# else:
#     print(False)

# def test_time(func):
#     def wrapper(*args,**kwargs):
#         t1 = time.time()
#         result = func(*args,**kwargs)
#         t2 = time.time()
#         print("{}函数:{}".format(func.__name__,t2-t1))
#         return result
#     return wrapper
#
# @test_time
# def test01():
#     time.sleep(5)
#     test02()
#
# @test_time
# def test02():
#     time.sleep(2)
# t11 = time.time()
# test01()
# t22 = time.time()
# print("实际用时:{}".format(t22-t11))

# a = []
# if a:
#     print(True)
a = [{"a":1, "n": 1}]
c = tuple(a)
print(c)


