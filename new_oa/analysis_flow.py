import xml
import re
from connectDB import ConnDB
from xml.dom.minidom import parse



sql = "select data from lcsz"
# db = ConnDB('dm', 'HCOA', '123456789', '172.16.12.230')
db = ConnDB('dm', 'HCOA', '123456789', '127.0.0.1')
# db = ConnDB('mysql', 'root', 'root', '127.0.0.1',database='hcitdata')
result = db.execute_sql(sql)


def get_flow_info():
    pat = r'<process id=".*" name="(.*?)".*?>'
    res = result.fetchone()
    # print(res)
    # if res:
    if res:
        res_str = res[0]  # 从返回的元祖中获取数据
        name_list = re.findall(pat, res_str)
        if len(name_list):
            # print(len(res_str))
            print(name_list)
            return name_list[0], res_str
        else:
            print("未解析到流程名称")
            return None,None
    else:
        return None, None


def create_flow_xml():
    while True:
        name, data = get_flow_info()
        if name is None:
            break
        with open('./flow_data/' + name + '.xml', mode='w', encoding='utf-8') as f:
            f.write(data)

# create_flow_xml()


class Flow():

    current_flow_id = None
    current_person_id = None

    def __init__(self, flowName):
        self.flowName = flowName

    def get_current_flow(self):
        pass

    def get_all_flow(self):
        print(self.current_flow_id)

    def get_last_flow(self):
        pass

    def get_current_person(self):
        pass

    def get_last_person(self):
        pass

    def set_flow_id(self, flow_id):
        Flow.current_flow_id = flow_id

    def set_person_id(self, person_id):
        Flow.current_person_id = person_id


DomTree = parse("./flow_data/参阅件流程.xml")
collection = DomTree.documentElement
# booklist = collection.getElementsByTagName("process")
# start_list = collection.getElementsByTagName("startEvent")
# user_list = collection.getElementsByTagName("userTask")
# all_list = collection.childNodes
# print(all_list[1])


def get_node_info(xml_obj):
    node_list = []
    flow_list = []
    ele_list = xml_obj.getElementsByTagName("process")  # 获取process节点标签元素
    if ele_list.length:  # 判断是否获取成功，如果成功则继续分解
        for ele in ele_list[0].childNodes:  # 循环获取process节点的各个字节点（流程节点）
            if ele.nodeName in ["startEvent","userTask","endEvent"]:
                ele_info = {"id": ele.getAttribute("id"), "name": ele.getAttribute("name"), "outgoing": [x.childNodes[0].nodeValue for x in ele.getElementsByTagName("outgoing")]}
                node_list.append(ele_info)
            elif ele.nodeName == "sequenceFlow":
                flow_info = {"id": ele.getAttribute("id"), "sourceRef": ele.getAttribute("sourceRef"), "targetRef": ele.getAttribute("targetRef")}
                flow_list.append(flow_info)
        return node_list, flow_list


def get_flow_list(xml_obj):
    node_list, flow_list= get_node_info(xml_obj)
    flow_name_list = []

    def get_sourceRef_targetRef(flow_id):
        def get_flow_info(id):  #根据flow_id获取连线信息
            for sequenceFlow in flow_list:
                if sequenceFlow["id"] == id:
                    sourceRef = sequenceFlow.get("sourceRef")
                    targetRef = sequenceFlow.get("targetRef")
                    if sourceRef and targetRef:
                        return sourceRef, targetRef
            else:
                return ("", "")
        if type(flow_id) is str:
            return [get_flow_info(flow_id)]
        elif type(flow_id) is list:
            flows = []
            for id in flow_id:
                flow = get_flow_info(id)
                flows.append(flow)
            return flows


    def getFlowIdByNode(Flow_id):  # 根据flow_id获取节点
        name_info_list = []
        target_id_list = [x[1] for x in get_sourceRef_targetRef(Flow_id)]
        for node in node_list:
            print("123:",node["id"])
            id = node["id"]
            if id in target_id_list:
                name_info_list.append((node["name"], id))
        return name_info_list

    def get_start_node():  # 获取开始节点
        for node in node_list:
            if node["id"] == "startNode1":
                for flow_id in node["outgoing"]:
                    if get_sourceRef_targetRef(flow_id)[0][1]:
                        return flow_id
                    else:
                        continue

    def getNodeIdByNextFlowId(NodeId):
        NextFlowId_list = [x["outgoing"] for x in node_list if x['id'] in NodeId][0]
        return NextFlowId_list

    flow_id = get_start_node()
    for i in range(len(node_list)):
        # print(get_node_name(flow_id))
        node_info_list = getFlowIdByNode(flow_id)
        node_names = [name[0] for name in node_info_list]
        node_ids = [id[1] for id in node_info_list]
        node_length = len(node_names)
        if node_length == 1:
            if len(flow_name_list) == 0:
                flow_name_list.append(node_names)
                flow_id = getNodeIdByNextFlowId(node_ids[0])
                continue
            for flow in flow_name_list:
                print("flow:",flow)
                flow.append(node_names)
                flow_id = getNodeIdByNextFlowId(node_ids[0])
        elif node_length > 1:
            name_list_len = len(flow_name_list)
            for x in range(name_list_len):
                print("x:", x)
                flow_name_list.append(flow_name_list[x])
                print("flow_name_list:",flow_name_list)
            # for n in range(node_length):
            i = 0
            for node_name in node_names:
                print(i)
                flow_name_list[i] = flow_name_list[i] + [node_name]
                # tmp_list.append(node_name)
                # flow_name_list.append(tmp_list)
                # print("tmp_list%a:"%i, tmp_list)
                i += 1
            flow_id = getNodeIdByNextFlowId(node_ids)
    return flow_name_list


print(get_flow_list(collection))
# print(get_flow_list(Flow_1o2rfcf).)
# a = [["a"]]
# for m in range(len(a)):
#     a.append(a[m])
# n = 0
# print(id(a[0]), id(a[1]))
# for i in ("b", "c"):
#     a[n] = a[n] + i
#
#     n += 1
# print(a)