# 练习
# 开发者:汪川
# 开发时间: 2021/4/4 20:55
"""key的判断"""
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']  # 删除指定的key—value对
# scores.clear() #清空字典的元素
print(scores)

scores['陈六'] = 100  # 修改元素
print(scores)
