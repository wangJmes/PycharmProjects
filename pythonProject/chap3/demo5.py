# 练习
# 开发者:汪川
# 开发时间: 2021/3/10 16:49
# 比较运算符
a, b = 10, 20
print('a>b吗？', a > b)
print('a<b吗？', a < b)
print('a>=b吗？', a >= b)
print('a<=b吗？', a <= b)
print('a=b吗？', a == b)
print('a!=b吗？', a != b)

a = 10
b = 10
print(a == b)  # True 说明，a，b的value 相等
print(a is b)  # True 说明, a,b的id标识 相等
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # value-->True
print(lst1 is lst2)  # id -->False
print(id(lst1))
print(id(lst2))
print(a is not b)  # False a的id与b的id不相等
print(lst1 is not b)  # True lst1的id与lst2的id相等
