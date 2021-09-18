#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 11:31
def get_count(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


if __name__ == '__main__':
    s = 'hellopython,hellojava,hellogo'
    ch = input('请输入用统计的字符:')
    count=get_count(s,ch)
    print(f'{ch}在{s}中的个数为{count}')