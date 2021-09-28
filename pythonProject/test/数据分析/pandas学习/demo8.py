#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 2021/9/27 11:35
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#  设置显示最大列、宽等参数，消除打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

movies = pd.read_csv("data/IMDB-Movie-Data.csv")
movies_Genre = movies['Genre']
# 统计分类的列表
temp_list = movies_Genre.str.split(',').tolist()  # [[],[],[]]
genre_list = list(set([i for j in temp_list for i in j]))

#  构造全为0的数组
zero_df = pd.DataFrame(np.zeros((movies.shape[0], len(genre_list))), columns=genre_list)
#  print(zero_df)

# 给每个电影出现分类的位置赋值1
for i in range(movies.shape[0]):
    zero_df.loc[i, temp_list[i]] = 1

#  print(zero_df.head(3))
#  统计每个分类的电影的数量和
genre_count = zero_df.sum(axis=0)
print(genre_count)

#  排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
#  画图
plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
