#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/28 18:11'
__author__ = 'Lee7'
# 列表变量调用+=本事执行extend，不会修改变量的引用
def demo(num,num_list):

    print("函数开始")

    num += num
    # 使用继承方法时，会更改外部函数值
    # num_list += num_list
    # num_list.extend(num_list)
    num_list = num_list + num_list
    print(num,num_list)
    print("函数完成")

gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num,gl_list)