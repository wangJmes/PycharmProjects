#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/19 17:36
from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=180)
plt.bar(range(len(quantity)), quantity, width=1)
# 设置x轴的刻度
_x = [i - 0.5 for i in range(13)]
_xtrick_labels = interval + [150]
plt.xticks(_x,_xtrick_labels)
plt.grid(alpha=0.5)
plt.show()
