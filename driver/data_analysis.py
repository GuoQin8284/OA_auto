import json

from config import BASE_DIR


def data_analysis(name):
    print("BASE_DIR:",BASE_DIR)
    fileName = BASE_DIR+"/test_data/" + name
    with open(file=fileName,mode="r",encoding="utf-8") as f:
        data = json.load(f)
        data_list = [(x,) for x in data]
        print(data_list)
        return data_list

data_analysis("send_text01.json")
