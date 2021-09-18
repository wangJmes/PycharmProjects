# 练习
# 开发者:汪川
# 开发时间: 2021/3/18 12:35
#  range()的三种创建方式

"""第一种创建方式，只有一个参数(小括号中只给了一个数)"""
r = range(10)
print(r)
print(list(r))  # 用查看range对象中的整数序列

'''第二种创建方式，给了两个参数(小括号里给了两个参数)'''
r = range(1, 10)
print(list(r))

"""第 三种创建方式，给了三个参数(小括号中只给了三个数)"""
r = range(1, 10, 2)
print(list(r))

"""判定指定的整数是否在序列内 in，not in"""
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)
