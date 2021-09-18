#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 23:15
import math

for i in range(100, 1000):
    if math.pow((i % 10), 3) + math.pow((i // 10 % 10), 3) + math.pow((i // 100), 3) == i:
        print(i)
