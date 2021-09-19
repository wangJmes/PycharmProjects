# 练习
# 开发者:汪川
# 开发时间: 2021/4/1 17:51
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)
print(lst)

# pop根据索引移除元素
lst.pop(1)
print(lst)
lst.pop()  # 如果不指定参数，删除列表最后一个元素

print('-----切片操作-删除至少一个元素，将产生一个新的列表对象------')
new_list = lst[1:3]
print('原列表', lst)
print('切片后的列表', new_list)

'''不产生新的列表对象，删除原列表中的内容'''
lst[1:3] = []
print(lst)

'''清楚列表中所有元素'''
lst.clear()
print(lst)
'''del语句删除列表'''
del list
#  print(lst)
