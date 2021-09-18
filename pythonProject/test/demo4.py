# 练习
# 开发者:汪川
# 开发时间: 2021/3/29 21:39

from math import log
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'yes'],
               [0, 1, 'no'],
               [0, 1, 'no'],
               [0, 0, 'no'],
               [0, 0, 'yes'],
               [0, 0, 'no']]
    labels = ['是否有房产', '是否有车']
    # 标签我们假设为是否买过某高端产品

    return dataSet, labels


# 计算信息熵    pi*logpi
# 先计算  pi   即yes 与 no 的概率
# 为了计算 pi，要先知道  总记录数  yes的数量   no的数量

def calcShannonEnt(dataSet):
    num = len(dataSet)  # 总共有多少行数据
    shannonEnt = 0.0  # 初始化信息熵
    labelCounts = {}
    for item in dataSet:  # 遍历整个数据集，每次取一行
        label = item[-1]  # 取该行最后一列的值  即标签
        if label not in labelCounts:  # 在字典中这个label是否存在
            labelCounts[label] = 0
        labelCounts[label] += 1  # { 'yes':2,'no':3 }
    for key in labelCounts:
        p = float(labelCounts[key] / num)  # 即每个标签所占的比重
        # print( p )
        shannonEnt -= p * log(p, 2)  # log base 2 计算信息熵
    return shannonEnt  # 返回根节点信息熵


# 测试整个数据集的熵
dataSet, labels = createDataSet()
shan = calcShannonEnt(dataSet)
print(shan)
'''
熵值越高，则混合的数据越多
'''
# 下面再增加一个分类
dataSet[7][-1] = '不确定'
shan = calcShannonEnt(dataSet)
print(shan)
