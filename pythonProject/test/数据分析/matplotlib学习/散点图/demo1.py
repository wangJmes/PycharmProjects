#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/18 21:43
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
y_3 = [11, 17, 16, 11, 12, 6, 7, 8, 9, 22, 14, 12, 15, 17, 16, 15, 15, 16, 12, 8, 16, 8, 6, 14, 12, 13, 15, 12, 13, 15,
       14]
print(len(y_3))
y_10 = [10, 15, 14, 15, 14, 16, 17, 18, 19, 22, 14, 10, 10, 15, 12, 9, 5, 6, 8, 8, 12, 9, 8, 12, 15, 17, 18, 19, 17, 15]
x_3 = range(1, 32)
x_10 = range(41, 71)
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(x_3, y_3,label='3月份')
plt.scatter(x_10, y_10,label='10月份')
# 设置x轴的刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ['3月{}日'.format(i) for i in x_3]
_xtick_labels += ['10月{}日'.format(i) for i in range(1,31)]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)
#  添加图例
plt.legend(loc='upper left',prop=my_font)
#  添加描述信息
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度',fontproperties=my_font)
plt.title('标题',fontproperties=my_font)
plt.show()
