#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 10:27
print(type(open('a.txt', 'r', encoding='utf-8')))
with open('a.txt', 'r', encoding='utf-8') as file:
    print(file.read())