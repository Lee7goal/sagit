# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/3 16:37'
__author__ = 'Lee7'

"""
open、read、write、close
"""
file = open("README.txt")

text = file.read()
print(text)
print(len(text))

print("-"*50)

text = file.read()
print(text)
print(len(text))

file.close()