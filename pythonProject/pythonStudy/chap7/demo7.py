# 练习
# 开发者:汪川
# 开发时间: 2021/4/4 21:28
#  字典生成式
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 120]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
