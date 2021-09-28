#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/25 21:52
"""pandas bool索引"""
import pandas as pd

# pandas读取csv中的文件
df = pd.read_csv("data/dogNames2.csv")
#  dataFrame中排序的方法
df = df.sort_values(by="Count_AnimalName")
#  大于800的狗的名字
df800 = df[df["Count_AnimalName"] > 800]
print(df800)
#  次数超过700并且名字的字符串的长度大于4的狗的名字
df700 = df[(df["Row_Labels"].str.len() > 4) & (df["Count_AnimalName"] > 700)]
