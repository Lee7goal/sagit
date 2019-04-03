# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/3 17:10'
__author__ = 'Lee7'
# 1.打开文件
file = open("README.txt","r+",encoding="utf-8")

while True:
    # 读取一行内容
    text = file.readline()
    # print(text)
    # 查询是否读到内容
    if not text:
        break
    print(text)
# 2.关闭文件
file.close()