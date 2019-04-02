# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/2 16:51'
__author__ = 'Lee7'

"""
异常概念
程序在运行时，解释器遇到错误时，会停止程序的执行，并提示错误信息，这就是异常
这个过程叫做抛出异常
使用try 和 except 代码捕获异常
try:
    尝试执行的代码
except:
    出现错误的处理
"""
# try:
#     num = int(input("请输入整数："))
# except:
#     print("输入的不是整数")
#
# print("-"*50)
# print("输入的数字为:",num)
try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数"))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num

    print(result)
except ZeroDivisionError:
    print("0不能被作为除数")
except ValueError:
     print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s"%result)
except IndentationError:
    print("回头看看缩进是不是错了")
else:
    # 没有异常才会执行的代码
    print("没有异常，恭喜")
finally:
    # 无论是否有异常，都会执行的代码
    print("="*50)