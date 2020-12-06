import json
from driver.action import Action
from module.fujian import Fujian
from module.read_opinion import ReadOpinion
from module.select_department import SelectDepartment
from module.send import Send

# 这是程序运行的入口，根据测试用例指定的测试数据，调用解析函数，dirver为浏览器驱动对象，fileName为测试数据路径
from module.verify_code import Verify_code

    # 获取host
from result.result import contains_text


def get_host_port():
    with open(file="./config.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)
        host = data["host"]
        return host

def analysis_data_func(driver,fileName):
    # with open(file="../test_data/{}".format(fileName), mode="r", encoding="utf-8") as f:
    #     data = json.load(f)

        file = fileName["fileName"]
        data_list = fileName["data"]
        tmp = analysis_action_func(driver,fileName=file,data_list=data_list)
        if tmp:
            return tmp

# 解析函数，根据传进来的json文件路径，查找到相关流程的接送文件，并根据json文件中定义的执行顺序，执行相关操作
def analysis_action_func(driver,fileName,data_list):
    with open(file="./flow_path/{}".format(fileName),mode = "r", encoding="utf-8") as f:

        # 读取json文件数据
        data = json.load(f)
        #解析order数据
        order = data["order"]
        #解析action数据，action为动作列表
        action_list = data["action_list"]
        # 解析路由
        path = data["path"]
        # 拼接url
        url = get_host_port() + path
        print("url:",url)
        # 打开url
        driver.get(url)
        # 根据order执行顺序，执行相关的动作
        for i in order:
            i = "%s"% i
            try:
                args = data_list[i]
            except Exception:
                args = None

            # print('args:',args)
            # 从动作列表中解析出即将动作的元素
            action = action_list[i]
            # 从动作元素中解析出动作id
            action_id = action[0]
            if len(action)>1:
                # 从动作元素中解析出元素定位信息
                action_ele = action[1]
            else:
                action_ele = ""
            # 执行动作
            tmp = open_func(driver=driver,action_id=action_id,action_ele=action_ele,args=args)
            # 如果tmp值为真，且当前循环是处于流程中最后一个步骤，则将函数的返回值返回
            if tmp and i == str(order[-1]):
                # print("tmp:",tmp)
                return tmp

    # 执行函数，根据action_id中指定的动作，执行相关的动作；action_ele为要操作的元素；args为参数，默认为None
def open_func(driver,action_id,action_ele,args):

    # 初始化对象
    action = Action(driver)
    serchName = SelectDepartment(driver)
    readOpinion = ReadOpinion(action)
    send = Send(driver)
    fujian = Fujian(action)
    verifyCode = Verify_code(action)

    # 输入动作
    if action_id == "input":
        action.input_text(action_ele,args)
    # 单击操作
    elif action_id == "click":
        action.click(action_ele)
    # 双击操作
    elif action_id == "double":
        print("action_ele",action_ele)
        action.double_click(action_ele)
    # 获取元素的文本
    elif action_id == "result":
        text = action.contains_text(action_ele)
        if text:
            return text
    # 在选择人员的弹窗中，查询指定的人员，并选择
    elif action_id == "serchName":
        serchName.SearchName(args)
    # 签署阅文意见
    elif action_id == "ReadOpinion":
        action.click(action_ele)
        return readOpinion.input_content_flow_path(args)
    # 发送流程
    elif action_id == "Send":
        return send.send_text_flow(args)
    # 添加附件
    elif action_id == "Fujian":
        return fujian.fileUpload_folw(args)
    # 判断是否需要输入验证码，如果需要输入则输入验证码
    elif action_id == "Verify_code":
        return verifyCode.verify_code_flow()

    elif action_id == "rText":
        return contains_text(args)
