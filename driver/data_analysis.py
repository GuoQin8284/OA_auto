import json


def data_analysis(name):
    fileName = "./test_data/" + name
    with open(file=fileName,mode="r",encoding="utf-8") as f:
        data = json.load(f)
        data_list = [(x,) for x in data]
        print(data_list)
        return data

# data_analysis("send_text01.json")
