#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/11 17:44
height = 170
weight = 50.5
bmi = weight / (height + weight)
print('您的身高是:' + str(height))
print('您的体重是:' + str(weight))
print('您的BMI是:' + '{:0.2f}'.format(bmi))
