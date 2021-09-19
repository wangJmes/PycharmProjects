# 练习
# 开发者:汪川
# 开发时间: 2021/4/21 20:59
print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(ord('杨'))

print(chr(97), chr(98))
print(chr(26472))

"""==与is的区别
==比较的是value
is比较的是id是否相等"""
a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)
print(a is b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))
