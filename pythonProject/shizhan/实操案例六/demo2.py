#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/13 10:00
lst = []
for i in range(5):
    goods = input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品:\n')
    lst.append(goods)
for item in lst:
    print(item)
cart = []
while True:
    num = input('请输入要购买的商品的编号:')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break
    if num == 'q':
        break  # 退出当前循环
print('您购物车里已经选好的商品为:')
"""for m in cart:
    print(m)"""
for i in range(len(cart) - 1, -1,-1):
    print(cart[i])
