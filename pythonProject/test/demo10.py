# 练习
# 开发者:汪川
# 开发时间: 2021/6/2 11:13
def cal(a):
    m = 1
    for i in range(1, a + 1):
        m = m * i
    return m


if __name__ == '__main__':
    n = int(input('输入：'))
print("%d" % sum(map(cal, range(1, n + 1))))
