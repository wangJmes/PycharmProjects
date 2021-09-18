#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 21:17
"""加法"""
import torch

x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(x + y)
print(torch.add(x, y))
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
print('----------------------------------------------')
# 执行的功能是y=y+x
y.add_(x)
print(y)
