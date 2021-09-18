#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/19 12:04
# -*- coding: utf-8 -*-
# 频数分布直方图
import matplotlib
from matplotlib import pyplot as plt

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        }
matplotlib.rc("font", **font)
a = [85, 131, 128, 115, 114, 100, 98, 89, 131, 125, 122, 132, 131, 150, 99, 89, 90, 98, 123, 121, 120, 122, 117, 119,
     114, 116, 117, 119, 132, 141, 123, 121, 110, 120, 99, 95, 106, 105, 108, 100, 102, 103, 136]
plt.figure(figsize=(20, 8), dpi=80)
# 计算组数 组距设置要合适 尽可能整除
d = 5  # 组距
num_bins = (max(a) - min(a)) // d  # 取整
print(len(a))
print((max(a) - min(a)) / d)
print((max(a) - min(a)) // d)
# 频数分布
# plt.hist(a,num_bins)
# 频率分布
plt.hist(a, num_bins, density=1)
# density=1，density=True
# 设置x轴刻度 步长为组距
plt.xticks(range(min(a), max(a) + d, d))
plt.grid()

plt.xlabel("电影时长")
plt.ylabel("频率")
plt.title("统计不同时长电影数")
plt.savefig("./movie.png")
plt.show()
