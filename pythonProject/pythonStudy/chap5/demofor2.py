# 练习
# 开发者:汪川
# 开发时间: 2021/3/18 15:59
"""输出100到999之间的水仙花数
举例：
153=3*3*3+5*5*5+1*1*1"""

for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    #  print(ge, shi, bai)
    if item == ge**3 + shi**3 + bai**3:
        print(item)
