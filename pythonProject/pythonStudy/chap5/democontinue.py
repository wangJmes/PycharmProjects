# 练习
# 开发者:汪川
# 开发时间: 2021/3/18 17:00
"""要求输出1到50之间的倍数"""
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

print('-----continue------')
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)
