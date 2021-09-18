#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 11:28
pwd = input('支付宝支付密码:')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，支付密码只能是数据')

print('------------------------------------------')
print('支付数据合法' if pwd.isdigit() else '支付数据不合法，支付密码只能是数据')

