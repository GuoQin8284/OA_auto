import os
import time


# 启动pytest
from environment.check_env import checkPyEnv


def setup_pytest():
    checkPyEnv() # 检查运行环境
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("{}启动pytest...".format(start_time))
    pytest = "pytest"
    allure_report = r"allure generate report/data -o report/html --clean"
    os.system(pytest)  # 启动pytest
    os.system(allure_report)  # 生成allure测试报告
    end_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("{} pytest执行完成!".format(end_time))


if __name__ == "__main__":
    setup_pytest()