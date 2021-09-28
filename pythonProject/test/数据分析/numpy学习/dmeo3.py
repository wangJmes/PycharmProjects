#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/20 12:50
import numpy as np

us_data = './youtube_video_data/US_video_data_numbers.csv'
uk_data = './youtube_video_data/GB_video_data_numbers.csv'

# 加载国家数据
us_data = np.loadtxt(us_data, delimiter=',', dtype='int')
uk_data = np.loadtxt(uk_data, delimiter=',', dtype='int')

#  添加国家信息
#  构造全为0的数据
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)
#  构造全为1的数据
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)

#  分别添加一列全为0,1的数组
us_data = np.hstack((us_data,zeros_data))
ones_data = np.hstack((uk_data,ones_data))

#  拼接两组数据
final_data = np.vstack((us_data, ones_data))
print(final_data)
