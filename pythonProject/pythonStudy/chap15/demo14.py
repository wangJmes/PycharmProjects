#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 10:44
with open('logo.png', 'rb') as src_file:
    with open('copy2log.png', 'wb') as target_file:
        target_file.write(src_file.read())
