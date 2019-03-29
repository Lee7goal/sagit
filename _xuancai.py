#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 20:01'
__author__ = 'Lee7'
import random
# 函数的返回值的作用是，一个函数执行结束后，告诉调用者一个结果
# return 返回结果
# 调用函数以放，可以使用变量来接受函数的返回结果
def choice():
    num1 = random.randint(1,150)
    num2 = random.randint(1,20)
    print(num1,num2)
