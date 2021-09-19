# 练习
# 开发者:汪川
# 开发时间: 2021/4/1 16:46
lst = [10, 20, 30, 40, 50, 60, 70, 80]
#  print(lst[1:6:1])
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段:', id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])

print('-----步长为负数的情况-------')
print('原列表：', lst)
print(lst[::-1])
print(lst[7::-1])
# start=6,stop=0,step=-2
print(lst[6:0:-2])
