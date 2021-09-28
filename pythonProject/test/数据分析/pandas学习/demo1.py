#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/24 11:50
import pandas as pd

# pandas读取csv中的文件
df = pd.read_csv("data/dogNames2.csv")
#  print(df)
#  dataFrame中排序的方法
df = df.sort_values(by="Count_AnimalName")
# pandas取行或者列的注意点
#  -方括号写数组，表示取行，对行进行操作
#  -方括号写字符串，表示取列，对列进行操作
print(df[:20])
print('-----------取列------------------------')
print(df[:20]['Row_Labels'])  # Series类型


