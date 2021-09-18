#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/6 16:22
asc_or_desc = input('请选择(0.升序 1.降序):')
print(type(asc_or_desc))
if asc_or_desc == '0':
    asc_or_desc_bool = False
    print(asc_or_desc_bool)
else:
    asc_or_desc_bool = True
    print(asc_or_desc_bool)