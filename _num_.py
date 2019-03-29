#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 17:57'
__author__ = 'Lee7'
def sum_2_num():
    """对两个数字的求和"""
    print("下面进行加法测试")
    sum1 = float(input("输入第一个数字:"))
    sum2 = float(input("请输入第二个数字:"))

    result = sum1 + sum2

    print("%.2f" % result)
def minus_2_num():
    """对两个数字进行减法"""
    print("下面进行减法测试")
    sum1 = float(input("输入第一个数字:"))
    sum2 = float(input("请输入第二个数字:"))

    result = sum1 - sum2
    print("%.2f" % result)
def multi_2_num():
    """对两个数字进行乘法"""
    print("下面进行乘法测试")
    sum1 = float(input("输入第一个数字:"))
    sum2 = float(input("请输入第二个数字:"))

    result = sum1 * sum2
    print("%.2f" % result)
def divi_2_num():
    """对两个数字进行除法"""
    print("下面进行除法测试")
    sum1 = float(input("输入第一个数字:"))
    sum2 = float(input("请输入第二个数字:"))
    if sum1 == 0:
        print("error")
        quit()
        result = sum1 / sum2
    print("%.2f"%result)
