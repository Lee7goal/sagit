# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/1 19:27'
__author__ = 'Lee7'

# python中的MRO
# python 中针对类提供了一个内置属性 __mro__可以查看方法搜索顺序
# MRO 时method resolution order 主要用于再多继承时判单继承方法属性和调用路径
class Far:
    def test(self):
        print("A——测试方法")

    def demo(self):
        print("A——演示方法")
class Mot:
    def test(self):
        print("M---测试方法")
    def demo(self):
        print("M——演示方法")

class Son(Far,Mot):
    def __del__(self):
        return "臣妾记不住啊"

sb = Son()
sb.demo()
sb.test()

# 确定c类对象调用方法的顺序
print(sb.__mro__)