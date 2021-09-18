#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 16:59
def calc(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        if b != 0:
            return div()
        else:
            return '除数不能为0'


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == '__main__':
    a = int(input('请输入第一个整数:'))
    b = int(input('请输入第二个整数:'))
    op = input('请输入运算符:')
    print(calc(a, b, op))
