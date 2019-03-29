#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/15 15:41'
__author__ = 'Lee7'
xiaoming_dict = {"name":"小明",
                 "name123":"包子"
                 }

# 1.取值
print(xiaoming_dict["name"])
print(xiaoming_dict["name123"])
# 2.增加/修改
xiaoming_dict["jjlenth"] = 10
# 如果key存在，回修改已经存在的key值
xiaoming_dict["name"] = "白无迹"
print(xiaoming_dict)
# 3.删除
del xiaoming_dict["name"]
xiaoming_dict.pop("name123")
print(xiaoming_dict)