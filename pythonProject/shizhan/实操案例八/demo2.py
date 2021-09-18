#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 11:10
scores = (('广州恒大', 72), ('北京国安', 70), ('上海上港', 66), ('江苏苏宁', 53), ('山东鲁能', '51'))
for index, item in enumerate(scores):
    print(index + 1,'.', end=' ')
    for score in item:
        print(score,end=' ')
    print()

