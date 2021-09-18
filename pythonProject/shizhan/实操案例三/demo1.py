#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/12 10:18
def fun():
    num = int(input('请输入一个十进制的整数:'))  # 将str类型转换成int类型
    print(num, '的二进制数为', bin(num))  # 第一种写法，使用了个数可变的位置参数
    print(str(num) + '的二进制数为' + bin(num))  # 第二种写法
    print('%s的二进制数为:%s' % (num, bin(num)))  # 第三种写法，格式化字符串
    print('{0}的二进制为{1}'.format(num, bin(num)))  # 第三种写法，格式化字符串
    print(f'{num}的二进制数为:{bin(num)}')  # 第三种写法，格式化字符串
    print('---------------------------------------------------------')
    print(f'{num}的八进制数为:{oct(num)}')
    print(f'{num}的十六进制数为:{hex(num)}')


if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('只能输入整数，请重新输入')
