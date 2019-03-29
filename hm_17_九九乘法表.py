#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 16:08'
__author__ = 'Lee7'
def multiple_table():
    # 输出九九乘法表
    row = 1
    while row<=9:
        col = 1
        while col <=row:
           # print("*",end="")
            print("\t%d * %d = %d "%(row,col,row*col), end="")
            col += 1
        print("")
        row += 1
        # \n换行字符
        # \t垂直字符
        # \"转义字符