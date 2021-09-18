# 练习
# 开发者:汪川
# 开发时间: 2021/3/9 12:26
for item in range(1, 10):
    for j in range(1, item+1):
        print(j, '*', item, '=', item*j, '', end='')
    print()