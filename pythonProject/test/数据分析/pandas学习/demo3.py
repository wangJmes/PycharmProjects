#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/25 16:59
import pandas as pd
import numpy as np
import string

t = pd.Series(np.arange(10), index=list(string.ascii_uppercase[:10]))
print(t)
a = {string.ascii_uppercase[i]: i for i in range(10)}
print(a)
b = pd.Series(a, index=list(string.ascii_uppercase[5:15]))
print(b)
print(t.index)