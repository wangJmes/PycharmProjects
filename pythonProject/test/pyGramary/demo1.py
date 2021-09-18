#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/3 7:55
filename = 'demo1.txt'
students = []
english = []
with open(filename, 'r', encoding='utf-8') as file:
    student = file.readlines()
    print(student)
for item in student:
    d = dict(eval(item))
    students.append(d)
for item in students:
    d = item['english']
    english.append(d)
print(english)
