#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 17:09'
__author__ = 'Lee7'
name = "小明"
# hello() 需要先定义函数，才能使用函数


def hello():
    """打招呼"""
    a = 1
    while a<=5:
        print("今天见你第%d次了"%a)
        a += 1
        if a == 3:
            a += 1
            continue
    print("奇怪，怎么少了一次呢？")
print(name)
hello()
print(name*2)