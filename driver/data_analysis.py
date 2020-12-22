import json

from config import BASE_DIR


def data_analysis(name):
    print("BASE_DIR:", BASE_DIR)
    fileName = BASE_DIR+"/test_data/" + name
    with open(file=fileName, mode="r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = [(x,) for x in data]
        print(data_list)
        return data_list

def lc_data(filename, lcName):
    data_list = data_analysis(filename)
    for i in data_list:
        if i[0]["gwlc"] == lcName:
            data = i[0]["data"]
            print("data", data)
            return data

lc_data("swgl_data.json","收文登记")
