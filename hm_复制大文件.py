#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/3 17:50'
__author__ = 'Lee7'
# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/3 17:34'
__author__ = 'Lee7'
import os
# 打开文件
file1 = open("README.txt","r+",encoding="utf-8")
file2 = open("TEST.txt","w+",encoding="utf-8")

while True:
    # 读取内容
    a = file1.readline()
    # 写入内容
    # file2.write(a)
    # 判断是否读取到内容
    if not a:
        break
    # 写入内容
    file2.write(a)

file1.close()
file2.close()
# os.remove("23323.txt")
print(os.listdir("."))
print(os.path.isdir(".idea"))
print(os.path.isdir("choujiang.py"))
# os.mkdir("大西瓜")
print(os.listdir("."))
os.rmdir("大西瓜")
