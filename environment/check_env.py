#!/usr/bin/python3
# -*- coding=utf-8 -*-
import os

from config import BASE_DIR


def read_package(pathname="python_package"):
    with open(file=BASE_DIR + os.sep + "environment" +  os.sep + "{}".format(pathname)) as f:
        data = f.readlines(-1)
        data_list = [x.replace("\n","").split("==") for x in data]
        data_dict = [{"{}".format(x[0]): "{}".format(x[-1])} for x in data_list]
        print(data_dict)
        return data_dict

def checkPyEnv():
    # env_list = os.system("pip list > echo")
    env_project = os.popen("pip list")
    env_list = env_project.read().splitlines()
    set_env = read_package()
    print("env_list",env_list)
    temp_cur_envName = [x.split(" ")[0] for x in env_list]
    print("temp_cur_envName:",temp_cur_envName)
    for set_env_key in set_env:
        key = list(set_env_key.keys())[0]
        value = set_env_key["key"]
        print("set_env_key.keys():",key)
        if key in  temp_cur_envName:
            pass
        else:
            os.system("pip install {}=={}".format(key,value))

if __name__ == "__main__":
    checkPyEnv()
    read_package()