#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 2021/9/28 10:10
import pandas as pd

#  设置显示最大列、宽等参数，消除打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

df = pd.read_csv('data/directory.csv')
grouped = df.groupby(by="Country")
print(grouped)

# DataFrameGroupBy
# 可以进行遍历
# for i, j in grouped:
#     print(i)
#     print("*" * 100)
#     print(j)
#     print("*" * 100)
# 调用聚合方法
print(grouped["Brand"].count())
