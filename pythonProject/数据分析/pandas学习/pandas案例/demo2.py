#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 2021/9/30 10:40
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df_bj = pd.read_csv("./datas/pm2.5/BeijingPM20100101_20151231.csv")
df_sh = pd.read_csv("./datas/pm2.5/ShanghaiPM20100101_20151231.csv")
print(df_bj.head(1))
print(df_bj.info())
print('*' * 100)
print(df_sh.head(1))
print(df_sh.info())
