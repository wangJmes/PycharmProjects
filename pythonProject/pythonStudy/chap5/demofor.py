# 练习
# 开发者:汪川
# 开发时间: 2021/3/18 15:37
for item in 'python':
    print(item)
#  range()产生一个整数序列--》也是一个可迭代对象
for i in range(10):
    print(i)

#  如果在循环体中不需要使用到自定义变量，可将自定义变量写为“-"
for _ in range(5):
    print('人生苦短，我用python')  # range()函数可用于循环次数
print('使用for循环，计算1到100之间的偶数和')
sum = 0
for item in range(101):
    if item % 2 == 0:
        sum += item
    item += item
print(sum)
