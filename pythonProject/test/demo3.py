# 练习
# 开发者:汪川
# 开发时间: 2021/3/17 17:50
import pandas as pd
import xlrd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
d2 = pd.DataFrame(s)
d.head()
d.describe()
pd.read_excel('data.xls')
#  pd.read_csv('data.csv', encoding='utf-8')
