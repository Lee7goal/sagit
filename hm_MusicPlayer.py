#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/2 15:23'
__author__ = 'Lee7'

# 单例--让类创建的对象，在系统中只有唯一的一个实例
"""
1.定义一个类属性，初始值是None，用于记录单例对象的引用
2.重写new
3.如果类属性isNone，调用父类方法分配空间，并在类属性中记录结果
4.返回类属性中记录的对象引用
"""
class MusicPlayer(object):
    instance = None
    init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("创建程序中...")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag is False:
            print("程序初始化...")
            MusicPlayer.init_flag = True
        return
    pass
#创建多个对象
player1 = MusicPlayer()
player2 = MusicPlayer()
player3 = MusicPlayer()

print(player1)
print(player2)
print(player3)

