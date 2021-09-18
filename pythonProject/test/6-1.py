# 拉格朗日插值法
import pandas as pd
from scipy.interpolate import lagrange


inputfile = './missing_data.xls'
outputfile = './missing_data_processed.xls'
data = pd.read_excel(inputfile, header=None)


def ployinterp_column(s, n, k=5):
    y = s.reindex(list(range(n - k, n)) + list(range(n + 1, n + 1 + k)))  # 取数
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data.loc[j, i] = ployinterp_column(data[i], j)
data.to_excel(outputfile, header=None, index=False)
