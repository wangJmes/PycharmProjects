#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 12:26
import random

price = random.randint(1000, 1500)
print('今日竞猜商品为小米扫地机器人，价格在[1000-1500之间]')


def fun():
    global guess
    guess = int(input('请输入竞猜价格:'))


if __name__ == '__main__':
    fun()
    while True:
        if price == guess:
            print('猜对了')
            break
        elif price <= guess:
            print('大了')
            fun()
            continue
        else:
            print('小了')
            fun()
            continue
