#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/1 20:20'
__author__ = 'Lee7'

"""
在Python中的属性的获取存在一个向上查找机制

"""
class Tool:
    count = 0
    list_info = []
    def __init__(self,name):
        self.name = name
        Tool.list_info.append(self.name)
        Tool.count += 1
    def yichu(self):
        Tool.count -= 1
        Tool.list_info.remove(self.name)
a = Tool("水桶")
b = Tool("充气娃娃")
print(b.count)
b.yichu()
print(Tool.count)
print(Tool.list_info)
b.yichu()
print(Tool.count)
print(Tool.list_info)

