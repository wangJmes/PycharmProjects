# 练习
# 开发者:汪川
# 开发时间: 2021/3/15 17:17
score = int(input('请输入一个成绩:'))
#  判断
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
elif 0 <= score <= 59:
    print('E')
else:
    print('成绩无效')
