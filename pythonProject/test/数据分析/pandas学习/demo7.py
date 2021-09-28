#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 2021/9/27 10:42
import pandas as pd
from matplotlib import pyplot as plt

# pandas读取csv中的文件
movies_data = pd.read_csv("data/IMDB-Movie-Data.csv")
#  rating
rating = movies_data["Rating"]
print(rating)
#  rating的最大值最小值
max_rating = rating.max()
min_rating = rating.min()
#  计算组数
num_bin_list = [1.6]
i = 1.6
while i <= max_rating:
    i += 0.5
    num_bin_list.append(i)
print(num_bin_list)
#  绘制图形大小
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(rating, num_bin_list)
#  设置刻度
_x = [min_rating]
i = min_rating
while i <= max_rating + 0.5:
    i = i + 0.5
    _x.append(i)
plt.xticks(_x)
#  设置网格
plt.grid()
plt.show()
