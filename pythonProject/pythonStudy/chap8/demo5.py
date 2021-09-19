# 练习
# 开发者:汪川
# 开发时间: 2021/4/8 21:03
"""第一种创建方式使用{}"""
s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合中的元素不能重复
print(s)

"""第二种创建方式使用set()"""
s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 2, 3, 4])
print(s2)

s3 = set((1, 2, 6, 5, 4, 65))  # 集合中的元素是无序的
print(s3, type(s3))

s4 = set('Python')
print(s4)

s5 = set({12, 4, 56, 78, 44})
print(s5)

#  定义一个空集合
s6 = {}  # dict字典类型
print(type(s6))

s7 = set()
print(s7, type(s7))
