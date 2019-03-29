#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/12 13:46'
__author__ = 'Lee7'
# 收银员输入苹果的单价：元/斤
price = float(input("请输入购买物品价格："))

# 收银员输入购买苹果的重量，单位：斤
weight = float(input("请输入购买数量:"))

# 计算并且输出付款金额
money = price * weight

# 计算够不够买
myMoney = float(input("请输入你的余额:"))

if myMoney>money:
    print("购买成功，剩下了",myMoney-money,"元钱")
    print("-----"*7)
    print("购买凭条")
    print("购买物品:苹果","\n购买数量:",weight,"斤\n总金额:",money,"元\n购买日期:",__date__)
    print("-----"*7)
else:
    print("钱看起来不够呢，还是回家吧")


