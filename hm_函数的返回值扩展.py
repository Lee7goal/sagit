#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/28 16:42'
__author__ = 'Lee7'

# 一个函数执行返回多个结果
def measure():
    """返回当前的温度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")
    # 元祖可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # 如果需要返回多个数值，可以省略小括号
    return  temp,wetness

result = measure()
print(result)
# 相当不方便的办法
print(result[0])
print(result[1])
print(type(result))
# 可以使用多个变量，一次接受函数的返回结果
gl_temp,gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
