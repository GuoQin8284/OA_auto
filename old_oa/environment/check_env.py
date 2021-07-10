#!/usr/bin/python3
# -*- coding=utf-8 -*-
import os

from config import BASE_DIR


def read_package(pathname="python_package"):
    with open(file=BASE_DIR + os.sep + "environment" +  os.sep + "{}".format(pathname)) as f:
        data = f.readlines(-1)
        data_list = [x.replace("\n","").split("==") for x in data]
        data_dict = [{"{}".format(x[0]): "{}".format(x[-1])} for x in data_list]
        # print(data_dict)
        return data_dict

def checkPyEnv():
    print("正在检查运行环境...")
    env_project = os.popen("pip list")
    env_list = env_project.read().splitlines()
    set_env = read_package()
    temp_cur_envName = [x.split(" ")[0] for x in env_list]
    for set_env_key in set_env:
        key = list(set_env_key.keys())[0]
        value = set_env_key[key]
        try:
            if key in  temp_cur_envName:
                print("{} 已安装.".format(key))
            else:
                print("{} 未安装，正在安装...".format(key))
                os.system("pip install {}=={}".format(key,value))
                print("{} 已安装完成.".format(key))

        except Exception as f:
            print("运行环境检查失败...")
            raise f
    print("运行环境检查完成！")

if __name__ == "__main__":
    checkPyEnv()
    read_package()