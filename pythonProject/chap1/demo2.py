# 练习
# 开发者:汪川
# 开发时间: 2021/3/3 17:27
# 转义字符
print('hello\nworld')  # \ +转义功能的首字母  n-->newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')  # world将hello进行了覆盖
print('hello\bworld')  # \b是退格，将O退没了

print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符之前加上r，或R
print(r'hello\n world')
# 注意事项，最后一个字符不能是反斜杠
# print(r 'hello\n world\')
print(r'hello\n world\\')
