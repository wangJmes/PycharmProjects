# 练习
# 开发者:汪川
# 开发时间: 2021/8/23 17:12
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0}，今年{1}岁'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))
print(stu)
print(type(stu))
