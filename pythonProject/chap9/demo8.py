# 练习
# 开发者:汪川
# 开发时间: 2021/4/21 20:50
s = 'hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello,Python,Python,Python'
print(s.replace('Python', 'Java', 2))

lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Java', 'Python')
print(''.join(t))

print('*'.join('Python'))
