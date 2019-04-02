# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/2 15:04'
__author__ = 'Lee7'

class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # return super().__new__(cls) 下面方法可能更好调用，但是封装内部怎么调用呢
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        print("播放器初始化")

#创建播放器对象
player = MusicPlayer()
print(player)