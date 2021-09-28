#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 2021/9/26 21:20
import pandas as pd
import numpy as np

# pandas读取csv中的文件
movies_data = pd.read_csv("data/IMDB-Movie-Data.csv")
#  评分的平均分
rating_mean = movies_data["Rating"].mean()
#  获取导演人数
print('----------------导演人数---------------------------------')
#  print(movies_data["Director"].str.split(",").tolist())
print(len(movies_data["Director"].unique()))
#  演员人数
print('-----------------演员人数----------------------------------------')
actor_list = movies_data["Actors"].str.split(",").tolist()
actor_nums = len(set([i for j in actor_list for i in j]))
#  np.array(actor_list).flatten()  #二维转一维
print(actor_nums)
#  电影时长的最大值最小值
print('----------------电影时长最大最小值----------------------------------------')
max_runtime = movies_data["Runtime (Minutes)"].max()
max_runtime_index = movies_data["Runtime (Minutes)"].argmax()
print(max_runtime)
print('-------------------------------------------')
print(max_runtime_index)
min_runtime = movies_data["Runtime (Minutes)"].min()
print('-----------------------------------------------')
print(min_runtime)
min_runtime_index = movies_data["Runtime (Minutes)"].argmin()
print('------------------------------------------------')
print(min_runtime_index)
print('--------------------------------------------')
runtime_median = movies_data["Runtime (Minutes)"].median()
print(runtime_median)

