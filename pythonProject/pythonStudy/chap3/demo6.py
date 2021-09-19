# 练习
# 开发者:汪川
# 开发时间: 2021/3/10 17:18
#  布尔运算符
print('------and---------')
a, b = 1, 2
print(a == 1 and b == 2)
print(a == 1 and b < 2)
print(a == 1 and b == 2)
print(a != 1 and b != 2)

print('------or---------')
print(a == 1 or b == 2)
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)

print('------not 对boo类型操作数取反---------')
f = True
f2 = False
print(not f)
print(not f2)

print('------in 与 not in---------')
s = 'hello world'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
