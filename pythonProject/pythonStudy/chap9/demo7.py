# 练习
# 开发者:汪川
# 开发时间: 2021/4/19 21:37
s='hello,python'
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三_'.isidentifier())
print('4.', '张三_123'.isidentifier())

print('5.', '\t'.isspace())

print('6.', 'abc'.isalpha())
print('7.', '张三'.isalpha())
print('8.', '张三1'.isalnum())

print('9.', '123'.isdecimal())
print('10.', '123四'.isdecimal())
print('11.', 'ⅠⅡⅢ'.isdecimal())

print('12.', '123'.isnumeric())
print('13.', '123四'.isnumeric())
print('14.', 'ⅠⅡⅢ'.isnumeric())

print('15.', 'abc1'.isalnum())
print('16.', '张三123'.isalnum())
print('17.', 'abc!'.isalnum())