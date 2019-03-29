#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/15 13:31'
__author__ = 'Lee7'
xiaoming = {
        "name":"小明",
        "age":18,
        "gender":True,
        "height":1.75
}
print(xiaoming)
# print(xiaoming.copy())
yuansu_list = []
for name in xiaoming.items():

    yuansu_list.append(name)
yuansu_list.sort()
print(yuansu_list)
