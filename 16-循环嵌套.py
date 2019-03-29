#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 13:47'
__author__ = 'Lee7'
# 九九乘法表
row = 1

while row<=5:
    #定义一个列的计数器
    col = 1
    while col<=row:
        print("*",end="")
        col += 1
    print("")
    row += 1