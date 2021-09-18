#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 11:24
phones = set()
for i in range(5):
    info = input(f'请输入第{i + 1}个朋友的姓名与手机号码:')
    phones.add(info)
for item in phones:
    print(item)
