#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 10:55
print('用户手机原有话费金额:8元')
money = int(input('请输入充值金额:'))
print(f'当前可用金额:\033[0;31m{money + 8}\033[m')
