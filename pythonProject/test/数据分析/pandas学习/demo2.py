#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/24 16:52
from pymongo import MongoClient
import pandas as pd

client = MongoClient()
collection = client["douban"]['movies']
data = collection.find()
data_list = []
for i in data:
    temp = {'MOVIE_ID': i['MOVIE_ID'], 'NAME': i['NAME'], 'DOUBAN_SCORE': i['DOUBAN_SCORE']}
    data_list.append(temp)
#  t1 = data[0]
#  t1 = pd.Series(t1)
#  print(t1)
df = pd.DataFrame(data_list)
#  显示前10行
df = df.head(10)
print(df)
print('--------------展示df的概览---------------------------------------')
print(df.info())
print('------------------------快速综合统计结果----------------------------------------')
print(df.describe().astype(int))