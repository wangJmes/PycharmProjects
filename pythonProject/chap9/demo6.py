# 练习
# 开发者:汪川
# 开发时间: 2021/4/19 21:22
s = 'hello world Python'
lst = s.split()
print(lst)
s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

"""rsplit()从右侧开始劈分"""
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))
