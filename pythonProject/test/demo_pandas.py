# 练习
# 开发者:汪川
# 开发时间: 2021/5/17 17:16
import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # 创建一个序列
print(s)
d = pd.DataFrame([['1', 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])  # 创建一个表
d2 = pd.DataFrame(s)
print(d2)
print(d.head())  # 预览前五行数据
print(d.describe())  # 数据基本统计量
