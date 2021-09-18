# 练习
# 开发者:汪川
# 开发时间: 2021/3/15 21:47
# 求线性方程组
from scipy.optimize import fsolve


def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]


result = fsolve(f, [1, 1])
print(result)
# 数值积分
from scipy import integrate


def g(x):
    return (1 - x ** 2) ** 0.5


pi_2, err = integrate.quad(g, -1, 1)
print(pi_2 * 2)
