import os
import time


# 启动pytest
def setup_pytest():
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("{}启动pytest...".format(start_time))
    pytest = "pytest"
    allure_report = r"allure generate report/data -o report/html --clean"
    os.system(pytest)
    os.system(allure_report)
    end_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("{} pytest执行完成!".format(end_time))


if __name__ == "__main__":
    setup_pytest()