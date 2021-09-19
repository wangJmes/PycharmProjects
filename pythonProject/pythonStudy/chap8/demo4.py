# 练习
# 开发者:汪川
# 开发时间: 2021/4/5 16:38

"""元组的遍历"""
t = ('Python', 'world', 98)
"""第一种获取元组的方式，使用索引"""
print(t[0])
print(t[1])
print(t[2])
#  print(t[3])  #IndexError:tuple index out of range
"""遍历元组"""
for item in t:
    print(item)
