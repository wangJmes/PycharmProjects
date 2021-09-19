# 练习
# 开发者:汪川
# 开发时间: 2021/4/8 21:16
s = {10, 20, 30, 40, 50, 60}
"""集合元素的判断操作"""
print(10 in s)
print(100 in s)
print(10 not in s)
"""集合元素的新增操作"""
s.add(80)  # 一次添加一个元素
print(s)
s.update({200, 400, 300})  # 一次添加多个元素
print(s)
s.update([100, 99, 8])
s.update((78, 64, 56))
print(s)

"""集合元素的删除操作"""
s.remove(10)
print(s)
s.discard(500)  # 无删除元素也不会报错
print(s)
s.pop()
s.pop()  # 随机删除一个参数
print(s)
s.clear()
print(s)