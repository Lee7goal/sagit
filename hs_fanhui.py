#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 20:26'
__author__ = 'Lee7'

def sum_2_num(num1,num2):
    """对两个数字的求和"""
    result = num1 + num2
    #  可以用返回值告诉调用的计算的结果
    return result
sum_result = sum_2_num(10,20)
print("计算结果:%d"%sum_result)
