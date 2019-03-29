#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/28 17:25'
__author__ = 'Lee7'

a = 23
b = 35
# 1.使用其他变量
# c = a
# a = b
# b = c
# 2.不使用其他变量
# a = a + b
# b = a - b
# a = a - b
# 解法3 - Python专用
a,b = (b,a)
a,b = b,a
print(a,b)

