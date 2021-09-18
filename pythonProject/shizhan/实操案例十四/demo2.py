#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 17:17
import datetime


def inputdate():
    indate = input('请输入开始日期:(20200808)后按回车:')
    # 去除首尾空格
    indate = indate.strip()
    datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:]
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')


if __name__ == '__main__':
    print('---------推算几天后的日期----------------')
    sdate = inputdate()
    in_num = int(input('请输入间隔的天数:'))
    fdate = sdate + datetime.timedelta(days=in_num)
    print('您推算的日期是:' + str(fdate).split()[0])  # 分割字符串取列表第一个元素
