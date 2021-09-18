#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/17 12:15
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 2, 2, 1, 4, 2, 2, 1, 2, 1, 1, 2, 3, 2, 1, 2, 2, 1]
plt.figure(figsize=(20, 16), dpi=100)
plt.plot(x, y,label='自己',color='orange',linestyle='-.')
plt.plot(x,y2,label='同桌',color='cyan',linestyle=':')
# 设置x轴的刻度
_xtick_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_labels, rotation=45, fontproperties=my_font)
plt.yticks(range(0, 9))
#  绘制网格,设置透明度,0-1
plt.grid(alpha=0.5,linestyle=':')
#  添加图例,这里的参数添加的是prop,loc指定位置
plt.legend(prop=my_font,loc='upper left')
# 显示
plt.show()
