#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 21:28
import torch

x = torch.rand(3, 5)
print(x)
print('------------切片---------------')
print(x[:, 1])
print(x[:, :3])
