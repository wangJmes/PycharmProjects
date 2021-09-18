#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 17:25
import random


def guess(num, guess_number):
    if num == guess_number:
        return 0
    elif guess_number > num:
        return 1
    else:
        return -1


if __name__ == '__main__':
    num = random.randint(1, 100)
    for item in range(10):
        guess_number = int(input('我心里有个数[1-100]请你猜一猜:'))
        result = guess(num, guess_number)
        if result == 0:
            print('恭喜您猜对了')
            break
        elif result == 1:
            print('大了')
        elif result == -1:
            print('小了')
    else:
        print('真笨，10次都没猜中')
