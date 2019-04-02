#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/1 18:17'
__author__ = 'Lee7'

class Far:
    def test(self):
        print("测试方法")
class Mot:
    def demo(self):
        print("演示方法")

class Son(Far,Mot):
    def __del__(self):
        return "臣妾记不住啊"

sb = Son()
sb.demo()
sb.test()
# 优先继承先继承的对象
