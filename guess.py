# -*- coding:utf-8 -*-
import random

number = random.randint(1,10)
number1 = int(input('请输入一个数字：'))
while number1 == number:
    print("猜对了")
    break
if number1 != number:
    print("猜错了,是否再来一次\n1.是  2.否")
    xuanze = int(input())
    if xuanze == 1:
        number1 = int(input('请再猜一次：'))
if number == number1:
    print("猜对了")
else:
    print("又猜错了，游戏结束！")
    quit()