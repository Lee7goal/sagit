#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/18 17:07'
__author__ = 'Lee7'

# 1.框架搭建
# 2.新增名片
# 3.显示所有名片
# 4.查询名片
# 5.查询成功后修改、删除名片
# 6.打包应用

while True:
    # 显示系统菜单
    print("*"*50)
    print("欢迎来到名片管理系统 version:beta1")
    print("【1】增加新名片")
    print("【2】显示全部")
    print("【3】查询名片")
    print("【0】退出系统")
    print("*" * 50)
    action = int(input("请选择需要使用的功能:"))
    print("你选择的操作是: 【%d】"%action)
    #根据用户选择的功能进行代码执行
    if action == 1:
        pass
    elif action == 2:
        pass
    elif action == 3:
        pass
    elif action == 0:
        print("退出成功")
        quit()