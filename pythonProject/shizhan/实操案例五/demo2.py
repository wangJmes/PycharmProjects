#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 21:43
for item in range(1, 4):
    user_name = input('请输入用户姓名:')
    user_pwd = input('请输入密码:')
    if user_name == 'admin' and user_pwd == '8888':
        print('登录成功')
        break
    else:
        print('用户名或密码不正确!!!')
        print(f'您还有{3-item}次机会')
else:
    print('对不起，三次输入错误，请联系后台管理员')
