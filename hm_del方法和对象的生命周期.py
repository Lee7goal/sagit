#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/30 18:55'
__author__ = 'Lee7'

class Cat:

    def __init__(self,new_name):

        self.name = new_name

        print("%s 来了"%self.name)

    def __del__(self):
        print("%s 我去了"% self.name)
tom = Cat("王大锤")
print(tom.name)
del tom
print("-"*50)

# 生命周期
# 一个对象从调用类名（）创建，生命周期开始
# 一个对象的del方法一旦被调用，生命周期结束
# 在对象的生命周期，可以访问对象属性，或者方法


