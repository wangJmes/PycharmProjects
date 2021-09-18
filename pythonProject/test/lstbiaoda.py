# 练习
# 开发者:汪川
lst = []
# 开发时间: 2021/4/4 21:42
for i in range(1, 11):
    lst.append(i * i)
print(lst)

lst2 = [i * i for i in range(1, 11)]
print(lst2)

lst3 = []
for i in range(1, 11):
    if i % 2 != 0:
        lst3.append(i)
print(lst3)

lst4 = [i for i in range(1, 11) if i % 2 != 0]
print(lst4)

lst5 = []
for i in 'ABC':
    for j in '123':
        lst5.append(i+j)
print(lst5)

lst6 = [i+j for i in 'ABC' for j in '123']
print(lst6)