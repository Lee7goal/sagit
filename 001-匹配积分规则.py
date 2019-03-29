#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/12 11:39'
__author__ = 'Lee7'
import random

# 随机一个玩家1的分数
player1 = random.randint(1200,1300)

# 随机一个玩家2的分数
player2 = random.randint(1200,1300)

print("玩家一分数:",player1)
print("玩家二分数:",player2)
# 积分变化
# 当玩家二胜利时
# 加分
# 扣分
winScore = round(25 + (player1 - player2)/20)
print("玩家二胜利时，得分为:",winScore)

loseScore = round((25 - (player2 - player1)/20)*0.7)
print("玩家一扣分:",loseScore)
# 当玩家一胜利时
winScore = round(25 + (player2 - player1)/20)
print("玩家一胜利时，得分为",winScore)

loseScore = round((25 - (player1 - player2)/20)*0.7)
print("玩家二扣分:",loseScore)
