#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/13 0:10
year = [82, 89, 88, 86, 85, 00, 99]
print('原列表', year)
for index, value in enumerate(year):
    #  print(index, value)
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))
print('修改之后的列表:', year)
# 列表的排序
year.sort()
print('排序之后的列表为', year)
