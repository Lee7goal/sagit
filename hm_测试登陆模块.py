#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/2 20:13'
__author__ = 'Lee7'
import hm_主动抛出异常

while True:
    try:
        print("欢迎来到英雄联盟")
        print("="*50)
        choice = input("请选择需要用的功能\n【1】登陆【2】注册   【0】退出")
        if choice == "1":
            hm_主动抛出异常.Login.denglu()
        elif choice == "2":
            hm_主动抛出异常.Login.reg()
        elif choice == "0":
            quit()
    except ValueError:
        print("大哥，请选择系统拥有的功能")