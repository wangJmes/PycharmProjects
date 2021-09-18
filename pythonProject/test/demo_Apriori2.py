# 练习
# 开发者:汪川
# 开发时间: 2021/5/5 12:27
from __future__ import print_function
import pandas as pd
from demo_apriori import *

inputfile = './menu_orders.xls'
outputfile = './apriori_rules.xls'
data = pd.read_excel(inputfile, header=None)
print(u'\n转换原始数据至0-1矩阵...')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数
b = map(ct, data.values)  # 用map方式执行
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用0填充
print(data)
print('-----------')
print(u'\n转换完毕。')
del b  # 删除中间变量b，节省内存

support = 0.2  # 最小支持度
confidence = 0.5  # 最小置信度
ms = '---'  # 连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

find_rule(data, support, confidence, ms).to_excel(outputfile)  # 保存结果
