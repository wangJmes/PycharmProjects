# 练习
# 开发者:汪川
# 开发时间: 2021/3/3 17:05
# 可以输出数字
print(4456)

# 可以输出字符串
print('hello world')
print("hello")

# 输出含运算符的表达式
print(3 + 1)

# 将数据输出文件中 ,注意点，1 ，所指定的盘存在， 2.使用file=fp
fp = open('D:/text.txt', 'a+')  # 如果文件不存在就创建，存在就在文件内容后面追加
print('hello world', file=fp)
fp.close

# 不进行换行输出（输出内容在一行当中）
print('hello', 'world', 'Python')
