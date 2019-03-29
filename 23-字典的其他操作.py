#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/15 16:12'
__author__ = 'Lee7'
xiaoming_dict = {
        "name":"白无迹",
        "age":18,
        "weight":65.0,
        "dick":18.5
}
# 1.统计键值对数量
print(len(xiaoming_dict))

# 2.合并字典
new_dict = {
    "height":1.75,
    "dick":21
}
xiaoming_dict.update(new_dict)
print(xiaoming_dict)
# 3.清空字典
# xiaoming_dict.clear()
# print(xiaoming_dict)


# 迭代遍历字典
# 变量K是每一次循环中，获取到的Key值对的key

#def paChong():
steal = {}
for k in xiaoming_dict:
    print("%s - %s"%(k,xiaoming_dict[k]))
    steal[k] = xiaoming_dict[k]
print(steal)
print(type(steal))