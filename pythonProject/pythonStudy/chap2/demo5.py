# 练习
# 开发者:汪川
# 开发时间: 2021/3/4 17:19
a = 3.14159
print(a, type(a))
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))