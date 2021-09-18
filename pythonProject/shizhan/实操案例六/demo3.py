#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/13 12:05
lst = []
filename = 'demo2.txt'


def fun():
    for i in range(5):
        goods = input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品:\n')
        lst.append(goods)
    with open(filename, 'w+', encoding='utf-8') as wfile:
        for item in lst:
            wfile.write(item+'\t')


cart = []
lst2 = []
while True:
    with open(filename, 'r', encoding='utf-8') as rfile:
        lst = rfile.readlines()
        if len(lst) == 0:
            fun()
        else:
            lst1 = (lst[0].split())
            for i in range(0, 10, 2):
                str1 = lst1[i] + lst1[i + 1]
                lst2.append(str1)
            num = input('请输入要购买的商品的编号:')
            for item in lst2:
                if item.find(num) != -1:
                    cart.append(item)
                    break
            if num == 'q':
                break  # 退出当前循环
print('您购物车里已经选好的商品为:')
for i in range(len(cart) - 1, -1, -1):
    print(cart[i])
