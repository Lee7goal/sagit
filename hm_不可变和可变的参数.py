#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/28 17:49'
__author__ = 'Lee7'

def demo(num,num_list):

    print("函数内部的代码")
    # 在函数内部针对参数使用赋值语句
    global gl_num
    gl_num = 98
    global gl_list
    gl_list = [7,8,9]
    num = 102
    num_list = [1,2,3]
    print(num,num_list)
    print("函数执行完成")

gl_num = 99
gl_list = [4,5,6]
demo(gl_num,gl_list)
print("函数外部为",gl_num,gl_list)