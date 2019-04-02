#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/2 20:19'
__author__ = 'Lee7'
"""
抛出异常，提供了一个Exception异常类
在开发时，如果满足特定业务需求时，希望抛出异常
1.创建一个Exception的对象
2.使用ralse关键字抛出异常对象
"""
def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码")
    # 2.判断密码长度 >= 8符合密码规则，返回密码
    if len(pwd) >= 8:
        return pwd
    # 3.如果＜8主动抛出异常
    print("密码不符合规则:")
    # 1.创建异常对象
    ex = Exception("密码长度不够")
    # 2.主动抛出异常
    raise ex
try:
    input_password()
except Exception as result:
    print(result)
