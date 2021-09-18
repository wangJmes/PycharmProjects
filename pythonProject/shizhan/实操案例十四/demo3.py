#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/17 17:45
import prettytable as pt


def showTicket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)


def orderTicket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row) == i+1:
            lst = [f'第{i+1}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)


orderTicket(13, 13, 5)
