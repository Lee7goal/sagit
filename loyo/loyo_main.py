#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/19 10:43'
__author__ = 'Lee7'
# print登陆界面
# input注册登录（无数据库时需要手动注册登陆）
# print登陆后获取好友列表
# append添加好友
# del删除好友
# quit退出
while True:
    print("*"*50)
    print("欢迎来到loyo beta1\n【1】登陆\n【2】注册\n\n【0】退出")
    print("*" * 50)
    shuru = input("请选择执行的功能")
    action = int(shuru)
    if action == 1:
        pass
    elif action == 2:
        pass
    elif action == 3:
        pass
    elif action == 0:
        quit()