#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 22:34
import random

num = random.randint(1, 100)
for i in range(1, 10):
    guess = int(input('我心中有个1-100之间的数，请你猜一猜:'))
    if guess < num:
        print('小了')
    elif guess > num:
        print('大了')
    else:
        print('恭喜你猜对了')
        break
print(f'你一共猜了{i}次')
if i <= 3:
    print('你真聪明')
elif i <= 7:
    print('还凑合')
else:
    print('智商堪忧')
