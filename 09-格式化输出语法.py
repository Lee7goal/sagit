#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/12 15:33'
__author__ = 'Lee7'

# 包含%的字符串，被称为格式化字符串
# %和不同的字符连用，不同类型的数据需要使用不同的格式化字符
# %s字符串
# %d有符号的十进制整数,%0?D可以补齐？位数
# %f浮点数，%。02f表示小数点后只显示两位
# %% 输出%
变量1 = 98.365
print("格式化字符串%.2f" % 变量1)
# 1.定义字符串变量name,输出 我的名字叫 小明，请多多关照
name = "是森马"
print("我的名字叫%s，请多多关照！"%name)

# 2.定义整数变量student_no,输出我的学号是000001
student_no = 1232123123
print("我的学号是%06d"%student_no)

# 定义小鼠price、weight、money
# 输出苹果单价9.00元/斤 购买了5.00斤，需要支付 45.00元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元/斤 购买了 %.2f 斤，需要支付 %.2f元"%(price,weight,money))
# 定义一个小鼠scale，输出数据比例是10.00%
scale = 0.10
print("数据比例是%.2f%%"%(scale*100))