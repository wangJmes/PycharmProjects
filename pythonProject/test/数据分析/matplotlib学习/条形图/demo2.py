#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/19 11:14
"""绘制横的条形图"""
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
a = ['敦刻尔克大撤退', '银魂', '战狼2', '星际特工：千星之', '黑白迷宫', '杀破狼·贪狼', '赛车总动员3：极', '十万个冷笑话2', '极盗车神', '二次初恋',
     '海边的曼彻斯特','地球：神奇的一天', '建军大业', '赛尔号大电影6', '心理罪', '猩球崛起：终极之战', '蜘蛛侠：英雄归来'
     ]
b = [1129.77, 281.7, 5.23, 4198.35, 127.34, 4696.92, 1508.18, 1801.03, 1339.11, 71.73, 92.94, 432.12, 4444.1, 744.71,
     3033.58, 640, 978]
# 设置图形大小
plt.figure(figsize=(8, 8), dpi=180)
plt.barh(range(len(a)), b, height=0.5, color='orange')
# 设置字符串到y轴
plt.yticks(range(len(a)),a, fontproperties=my_font)
plt.xticks(list(range(5000))[::500], fontproperties=my_font)
#  绘制网格,设置透明度
plt.grid(alpha=0.3)
plt.show()
