#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 18:20
import torch

#  创建一个全零矩阵并可指定数据元素的类型为long
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

#  直接通过数据创建张量
x = torch.tensor([2.5, 3.5])
print(x)

#  利用news_method方法得到一个张量
x = x.new_ones(5, 3, dtype=torch.double)
print(x)

#  利用rand_like方法得到相同张量尺寸的一个新张量，并且采用随机初始化来对其赋值
y = torch.rand_like(x, dtype=torch.float)
print(y)

#  得到张量的尺寸
print(x.size())

