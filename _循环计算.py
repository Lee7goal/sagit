#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/13 13:07'
__author__ = 'Lee7'
def xunhuanjs():
    import math
    # 实现0到100的数字求和
    i = 0
    result = 0
    ouShu = 0
    # while i < 100:
    #    i += 1
    #    if i%2 != 0:
    #        result += i
    # if i == 100:
    #    print(result)
    while i<10:
        #    if i>5:
        #        break
        if i %2 == 1:
            # 注意：在循环中，如果要使用continue这个关键字
            # 在使用之前，需要确认循环的技术是否修改
            # 不然会死循环
            i += 1
            continue
        print(i)
        i += 1
    print("over")

