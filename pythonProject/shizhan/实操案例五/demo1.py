#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 13:06
x = 97  # 代表a的ASCII值
for _ in range(26):
    print(chr(x), '--->', x)
    x += 1

print('---------------------')
x = 97
while x <= 122:
    print(chr(x), '-->', x)
    x += 1
