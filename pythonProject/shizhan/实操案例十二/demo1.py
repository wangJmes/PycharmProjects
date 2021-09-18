#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/14 21:29
import math

pi = math.pi


class Circle(object):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        area = pi * math.pow(self.r, 2)
        return area

    def get_perimeter(self):
        perimeter = 2 * pi * self.r
        return perimeter


if __name__ == '__main__':
    r = int(input('请输入r的值:'))
    circle = Circle(r)
    area = circle.get_area()
    perimeter = circle.get_perimeter()
    print('圆的面积为:{:.2f}'.format(area))
    print('圆的周长为:{:.2f}'.format(perimeter))
