#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 12:18
username = 296626472
password = 123
input_username = int(input('请输入用户名:'))
input_passwod = int(input('请输入密码:'))
print('登录成功' if username == input_username and password == input_passwod else '对不起，账号或密码错误')
