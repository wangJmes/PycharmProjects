#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 17:49
try:
    score = int(input('请输入分数:'))
    if 0 <= score <= 100:
        print(score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
