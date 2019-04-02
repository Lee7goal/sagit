#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/2 19:12'
__author__ = 'Lee7'

"""
当函数/方法执行出现异常，会将异常传送给函数/方法的调用一方
如果传递到主程序，仍然没有异常处理，程序才会被终止
需求：
定义函数demo1()提示用户输入一个整数并返回
定义函数demo2调用demo1
在主程序中调用demo2
"""
num = False
def demo1():
        return int(input("输入整数:"))
def demo2():
    return demo1()
# print(demo1())
while True:
    try :
        print(demo2())
    except ValueError:
        print( "大哥，你输错了,要不再试试？")