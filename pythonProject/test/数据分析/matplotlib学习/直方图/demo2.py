#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/19 12:15
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
a = [85, 131, 128, 115, 114, 100, 98, 89, 131, 125, 122, 132, 131, 150, 99, 89, 90, 98, 123, 121, 120, 122, 117, 119,
     114, 116, 117, 119, 132, 141, 123, 121, 110, 120, 99, 95, 106, 105, 108, 100, 102, 103, 136]
plt.figure(figsize=(20, 8), dpi=80)
# 计算组数
d = 5  # 组距
num_bins = (max(a) - min(a)) // d
plt.hist(a, num_bins,density=1)
# 设置x轴的刻度
plt.xticks(range(min(a), max(a)+d, d))
#  设置网格
plt.grid()
plt.xlabel("电影时长",fontproperties=my_font)
plt.ylabel("频率",fontproperties=my_font)
plt.title("统计不同时长电影数",fontproperties=my_font)
plt.show()
