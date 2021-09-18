#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/30 11:38
file = open('d.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
