# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/1 20:13'
__author__ = 'Lee7'

"""
定义一个工具类
没见工具都有自己的name
需求--知道使用这个类，创建了多少个工具对象
"""
class Tool:
    count = 0
    tools_list = []
    def __init__(self,name):
        self.name = name
        Tool.tools_list.append(self.name)
        Tool.count += 1

langtou = Tool("榔头")
chuizi = Tool("锤子")
qizi = Tool("起子")
print("现在有 %d 件工具"%Tool.count)
print("工具列表如下 %s "%Tool.tools_list)

