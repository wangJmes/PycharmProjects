#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/17 18:19
import datetime

a = '  20200808  '.strip()
b = a[0:4] + '-' + a[4:6] + '-' + a[6:]
date = datetime.datetime.strptime(b, '%Y-%m-%d')
print(str(date).split()[0])
