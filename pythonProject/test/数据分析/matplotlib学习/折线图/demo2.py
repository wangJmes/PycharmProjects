#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 22:57
import random
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# matplotlib里不支持中文显示
# 设置字体方式，这种方式在linux/windows下奏效
"""font = {'family': 'Microsoft YaHei',
        'weight': 'bold',
        'size': '10.0'}
matplotlib.rc('font',**font)
matplotlib.rc('font',family='Microsoft YaHei',weight='bold')
"""
# 设置字体方式
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(10, 8), dpi=80)
plt.plot(x, y)

# 调整x轴的刻度
_xtick_labels = ['十点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]
#  取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::6], _xtick_labels[::6], rotation=45, fontproperties=my_font)  # rotation旋转的度数


#  添加描述信息
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度 单位(℃)',fontproperties=my_font)
plt.title('10点到12点每分钟的气温变化情况',fontproperties=my_font)
plt.show()
