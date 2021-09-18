# 练习
# 开发者:汪川
# 开发时间: 2021/4/25 12:17

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(5))