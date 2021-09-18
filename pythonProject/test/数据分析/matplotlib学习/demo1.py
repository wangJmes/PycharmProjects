#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 22:22
from matplotlib import pyplot as plt

x = range(2, 26, 2)  # 数据在x轴的位置，是一个可迭代对象
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]  # 数据在y轴的位置，是一个可迭代对象

#  设置图片大小
plt.figure(figsize=(10, 8), dpi=100)
# 绘图
plt.plot(x, y)
# 设置x轴的刻度
_xticket_lables = [i / 2 for i in range(4, 49)]
plt.xticks(_xticket_lables[::3])
# 设置y轴的刻度
plt.yticks(range(min(y),max(y)+1))
# plt.xticks(range(2, 25))
#  保存
plt.savefig('./t1.png')  # 可以保存为svg这种矢量图格式，放大不会有锯齿
#  展示图形
#  plt.show()
