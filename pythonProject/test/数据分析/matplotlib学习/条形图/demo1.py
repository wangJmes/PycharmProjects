#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/18 19:13
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
x = ['敦刻尔克\n大撤退', '银魂', '战狼2', '星际特工：\n千星之', '黑白迷宫', '杀破狼\n·贪狼', '赛车总动员3\n：极', '十万个\n冷笑话2', '极盗车神', '二次初恋',
     '海边的\n曼彻斯特', '地球：\n神奇的一天', '建军大业', '赛尔号大电影6', '心理罪', '猩球崛起：\n终极之战', '蜘蛛侠：\n英雄归来'
     ]
y = [1129.77, 281.7, 5.23, 4198.35, 127.34, 4696.92, 1508.18, 1801.03, 1339.11, 71.73, 92.94, 432.12, 4444.1, 744.71,
     3033.58, 640, 978]
# 设置图形大小
plt.figure(figsize=(10, 5), dpi=180)
plt.bar(range(len(x)), y, width=0.5, color='orange')
# 设置字符串到x轴
plt.xticks(range(len(x)), x, rotation=90, fontproperties=my_font)
# 设置y轴的刻度
plt.show()
