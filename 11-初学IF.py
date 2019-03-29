#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/12 17:38'
__author__ = 'Lee7'
gongZi = int(input("请输入工资:"))
toDay = int(input("请输入今天几号："))
qianQian = 2000
gongziDay = 10
if toDay >= gongziDay :
# 先还信用卡的钱
    if gongZi - qianQian > 0:
        print("又可以happy了")
    else:
        print("没钱了再等30天")
else:
    print("等发工资"+"还有%s天"%(gongziDay-toDay))