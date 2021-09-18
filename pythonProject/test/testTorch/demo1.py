#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 18:13
from __future__ import print_function
import torch

x = torch.empty(5, 3)  # 创建一个5行3列的初始化矩阵
print(x)

x = torch.rand(5, 3)  # 有初始化的矩阵
print(x)
