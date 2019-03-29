#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/3/12 19:26'
__author__ = 'Lee7'

# 逻辑运算符
# and,or,not
# and 是两个判断同时成立返回Ture
# 条件1 and 条件2
# 条件1 与 条件2都成立
# or 是有一个判断成立就返回Ture
# 条件1 or 条件2
# 条件1或条件2成立就成立
# not 把一个条件取反
#定义一个整数变量age,编写代码判断年龄是否正确
age = 12000

# 要求人的年龄在0-120之间
if age>=0 and age<=120:
    print(True)
else:
    print(False)

if age>=0 or age<=120:
    print(True)
else:
    print(False)

if not age<=0 or age<=120:
    print(True)
else:
    print(False)

# 定义两个整数变量python_score、c_score编写代码判断
# 只要有一门合格就算合格
name = input("请输入考生姓名：")
id = int(input("请输入学号："))
python_score = int(input("请输入python成绩:"))
c_score = int(input("请输入C成绩："))

if python_score>=60 or c_score>=60:
    print("期末考试通过")
    print("-----"*7)
    print("打印成绩单")
    print("考生姓名：",name)
    print("考生学号：%06d"%id)
    print("Python成绩为",python_score)
    print("C++成绩为",c_score)
    print("恭喜通过期末考试！")
    print("-----" * 7)
else:
    print("不及格")
    print("-----" * 7)
    print("打印成绩单")
    print("考生姓名：", name)
    print("考生学号：%06d" % id)
    print("Python成绩为", python_score)
    print("C++成绩为", c_score)
    print("不要气馁，交了重修费再次来战")
    print("-----" * 7)

# 定义一个布尔变量 is_employee,
# 编写代码判断是否本公司员工
# 不是就禁止入内
is_employee = True

if is_employee==True:
    print("欢迎回到公司")
else:
    print("今天不对外人开放")