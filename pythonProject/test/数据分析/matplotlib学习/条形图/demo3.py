#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/19 11:32
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
a = ['敦刻尔克大撤退', '银魂', '战狼2', '猩球崛起3：终极之战']
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]
x_14 = list(range(len(a)))
bar_width = 0.2
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width * 2 for i in x_14]
# 设置图形大小
plt.figure(figsize=(8, 8), dpi=180)
plt.bar(x_14, b_14, width=0.2, color='orange',label='9月14日')
plt.bar(x_15, b_15, width=bar_width, color='red',label='9月15日')
plt.bar(x_16, b_16, width=bar_width, color='blue',label='9月16日')
#  设置图例
plt.legend(prop=my_font)
# 设置字符串到x轴
plt.xticks(x_15, a, fontproperties=my_font)
#  绘制网格,设置透明度
plt.grid(alpha=0.3)
plt.show()
