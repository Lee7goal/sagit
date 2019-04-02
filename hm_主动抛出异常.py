# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/2 19:46'
__author__ = 'Lee7'

"""
抛出raise异常
需求：
提示用户输入密码，如果长度少于8，抛出异常
用户登陆模块
用户输入密码
异常1：密码长度不够
异常2：密码不对
"""
zhanghao = None
password = None
class Login(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("创建进程中...")
            cls.instance = super().__new__(cls)
        return cls.instance
    @staticmethod
    def reg():
            global zhanghao
            global password
            zhanghao = input("请输入创建的账号")
            password = input("请输入密码")
            if len(zhanghao) < 5:
                print("账号至少要五位,请重新注册")
                zhanghao = None
            elif len(zhanghao) > 10:
                print("账号最多九位，请重新注册")
                zhanghao = None
            else:
                print("恭喜注册成功")
    @staticmethod
    def denglu():
        input_zhanghao = input("请输入您的账号")
        input_password = input("请输入你的密码")
        if input_zhanghao == zhanghao and input_password == password:
            print("登陆成功")
        else:
            print("用户名或密码错误")

