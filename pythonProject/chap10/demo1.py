# 练习
# 开发者:汪川
# 开发时间: 2021/4/23 12:20
def calc(a, b):
    c = a + b
    return c


result = calc(10, 20)
print(result)

res = calc(b=10, a=20)  # =左侧的变量名称为 关键字参数
print(res)
