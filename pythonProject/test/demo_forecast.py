# 练习
# 开发者:汪川
# 开发时间: 2021/5/24 17:58
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# 参数初始化
discfile = './arima_data.xls'
forecastnum = 10  # 预测数量
# 读取数据，指定日期列为指标 。pandas自动将‘日期’列识别为Datatime格式
data = pd.read_excel(discfile, index_col=u'日期')
# 时序图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data.plot()
plt.show()
# 自相关图
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(data).show()
# 平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF

print(u'原始序列的ADF检验结果为：', ADF(data[u'销量']))

# 差分后的结果
D_data = data.diff().dropna()
D_data.columns = [u'销量差分']
D_data.plot()  # 时序图
plt.show()
plot_acf(D_data).show()  # 自相关图
from statsmodels.graphics.tsaplots import plot_pacf

plot_pacf(D_data).show()  # 偏自相关图
print(u'差分时序的ADF检验结果为：', ADF(D_data[u'销量差分']))  # 平稳性检测

# 白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox

print(u'差分时序的白噪声检验结果为：', acorr_ljungbox(D_data, lags=1))  # 返回统计量和p值
from statsmodels.tsa.arima_model import ARIMA

# 定阶

pmax = int(len(D_data) / 10)
qmax = int(len(D_data) / 10)
bic_matrix = []  # bic矩阵
for p in range(pmax + 1):
    tmp = []
    for q in range(qmax + 1):
        try:  # 存在部分报错，所以用try来跳过报错
            tmp.append(ARIMA(data, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
bic_matrix = pd.DataFrame(bic_matrix)
print(bic_matrix)
p, q = bic_matrix.stack().astype(float).idxmin()
print(u'BIC最小的p值和q值为：%s，%s' % (p, q))
model = ARIMA(data, (p, 1, q)).fit()  # 建立ARIMA(0，1，1)模型
model.summary2()  # 给出一份模型报告
print(model.forecast(10))  # 作为期10天的预测。返回预测结果，标准误差，置信区间。

