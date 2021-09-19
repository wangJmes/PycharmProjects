# 练习
# 开发者:汪川
# 开发时间: 2021/3/18 16:17
"""从键盘录入密码，最多录入3次，如果正确就结束循环"""
flag = 0
for item in range(4):
    pwd = input("请输入密码:")
    flag += 1
    if pwd == "8888" and flag < 3:
        break
    elif flag < 3 and pwd != '8888':
        print('密码输入错误')
    else:
        print('您已经输入三次密码，输入次数上限')
