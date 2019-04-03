# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/3 17:34'
__author__ = 'Lee7'
# 打开文件
file1 = open("README.txt","r+",encoding="utf-8")
file2 = open("TEST.txt","w+",encoding="utf-8")

# 读取内容
a = file1.read()
# 写入内容
file2.write(a)

file1.close()
file2.close()