#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 2021/9/27 10:04
import pandas as pd
from matplotlib import pyplot as plt

# pandas读取csv中的文件
movies_data = pd.read_csv("data/IMDB-Movie-Data.csv")
#  rating
rating = movies_data["Rating"]
print(rating)
#  绘制图形大小
plt.figure(figsize=(20, 8), dpi=80)
d = 0.5  # 组距
#  rating的最大值最小值
max_rating = rating.max()
min_rating = rating.min()
num_bins = int((max_rating - min_rating) // d)
print(num_bins)
plt.hist(rating, num_bins, density=1)
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
