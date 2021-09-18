# 练习
# 开发者:汪川
# 开发时间: 2021/4/19 21:06
# 字符串大小写转换的方法
s = 'hello,python'
a = s.upper()  # 转成大写之后，会产生一个新的字符串对象
print(a, id(a))
print(s, id(s))
b = s.lower()
print(b, id(b))
print(s, id(b))
print(b == s)
print(b is s)

s2 = 'hello,Python'
print(s2.swapcase())

print(s2.title())