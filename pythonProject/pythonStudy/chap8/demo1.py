# 练习
# 开发者:汪川
# 开发时间: 2021/4/5 16:00
"""不可变序列，可变序列"""
"""可变序列 列表 字典"""
lst = [10, 20, 30]
print(id(lst))
lst.append(300)
print(id(lst))
"""不可变序列，字符串，元组"""
s = 'hello'
print(id(s))
s = s + '\tworld'
print(id(s))
print(s)

