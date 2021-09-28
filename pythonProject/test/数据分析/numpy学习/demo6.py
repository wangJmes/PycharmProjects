#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/23 22:12
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
us_data = './youtube_video_data/US_video_data_numbers.csv'
uk_data = './youtube_video_data/GB_video_data_numbers.csv'

# 加载国家数据
t_us = np.loadtxt(uk_data, delimiter=',', dtype='int')

# 取评论数
t_us_comments = t_us[:, -1]
# 取比5000小的数据
t_us_comments = t_us_comments[t_us_comments <= 5000]
print(t_us_comments.max(), t_us_comments.min())
d = 100
bin_nums = (t_us_comments.max() - t_us_comments.min()) // d
plt.hist(t_us_comments, bin_nums, density=1)
#  设置网格
plt.grid()
plt.show()
