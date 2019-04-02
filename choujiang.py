#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/1 20:39'
__author__ = 'Lee7'
import random
class Tool:
    """
    奖池权重如下
    少量金币:6
    中量金币:5
    大量金币:4
    少量钻石:5
    大量钻石:3
    如果采用字典格式则为"name":num
    权重计算: ([name]*num+[name1]*num1)
    """
    jiangchiqz = (["少量金币"]*6 + ["中量金币"]*5+["大量金币"]*4+["少量钻石"]*5+["大量钻石"]*3+["技能书"])
    beibao = []
    @staticmethod
    def choujiang():
        result = random.choice(Tool.jiangchiqz)
        Tool.beibao.append(result)
        # Tool.jiangchiqz.remove(result)
        print("抽到的奖品为 %s"%result)
    @staticmethod
    def baoguo():
            print("抽到了这些物品 %s"%Tool.beibao)

a = Tool()
a.choujiang()

a.baoguo()