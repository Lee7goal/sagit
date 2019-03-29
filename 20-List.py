#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/14 13:47'
__author__ = 'Lee7'
name_list = ["张三","李四","王五"]
#print(name_list[3])
name_list.append("白无迹")
print(name_list[3])
name_list.remove("张三")
name_list.append("白无迹")
print(name_list[2])
print(name_list.count("白无迹"))
print(name_list.index("白无迹"))
#name = "白无迹"
#del name_list["白无迹"]
print(name_list.count("白无迹"))
print(name_list.index("白无迹"))
name_list.insert(3,"楚玲")
print(name_list)
temp_list = ["夜宴","音乐","空间"]
name_list.extend(temp_list)
print(name_list)
list_len = len(name_list)
print("列表中包含%d个元素"%list_len)
num_list = [1,354,123,684,1338,461,534]
num_list.sort()
num_list.reverse()
print(num_list)
xiaoming = {
        "name":"小明",
        "age":18,
        "gender":True,
        "height":1.75
}