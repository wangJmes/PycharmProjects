# 练习
# 开发者:汪川
# 开发时间: 2021/3/18 16:49
a = 0
while a < 3:
    a += 1
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
