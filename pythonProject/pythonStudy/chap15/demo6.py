#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/28 18:08
src_file = open('logo.png', 'rb')
target_file = open('copyLogo.png', 'wb')
target_file.write(src_file.read())

target_file.close()
src_file.close()
