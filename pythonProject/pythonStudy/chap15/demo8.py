#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/28 18:08
file = open('c.txt', 'a')
# file.write('hello')
lst = ['java', 'go', 'python']
file.writelines(lst)
file.close()
