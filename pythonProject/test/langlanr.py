# 练习
# 开发者:汪川
# 开发时间: 2021/3/29 21:45
import pandas as pd
from scipy.interpolate import lagrange

inputfile = './catering_sale.xls'
outputfile = './sales.xls'
data = pd.read_excel(inputfile)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None


def ployinterp_column(s, n, k=5):
    y = s.iloc[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data.loc[j, i] = ployinterp_column(data[i], j)
data.to_excel(outputfile)
