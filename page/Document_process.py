# 发文处理单页面
from driver import action


class Document(action):
    def __init__(self):
        super().__init__()
        self.send_bt_box = "ID","wjbt"  # 发文标题输入框
        self.zsdw = "ID","zsdw"  # 主送单位
        self.csdw = "ID","csdw"  # 抄送单位
        self.mj = "ID","mj"  # 密级下拉选择框
        self.fs = "ID","fs"  # 份数输入框
        self.sava_btn = "XPATH"
