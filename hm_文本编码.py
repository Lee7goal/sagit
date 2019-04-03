#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/3 18:28'
__author__ = 'Lee7'

"""
ASCII编码，使用一个字节表示一个字符
8个0/1的排列组合方式一共有256种，也就是2**8
UTF-8编码格式(unicode)
计算机中使用1-6个字节
"""
# 引号前面的u可以告诉解释器这是一个utf-8
hello_str = u"hello世界"

print(hello_str)

for c in hello_str:
    print(c)