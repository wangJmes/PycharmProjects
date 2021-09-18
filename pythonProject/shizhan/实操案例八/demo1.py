#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 10:39
cof_list = ('蓝山','卡布奇诺','拿铁','皇家咖啡','女王咖啡','美丽与哀愁')
print('您好，欢迎光临小猫咖啡屋')
print('本店经营的咖啡有:', end='')
for index, item in enumerate(cof_list):
    print(index + 1, '.', item, end=' ')
print()
index = int(input('请输入您喜欢的咖啡编号:'))
print(f'您的咖啡到了{cof_list[index - 1]}好了，请您慢用...')
