# 练习
# 开发者:汪川
# 开发时间: 2021/8/23 16:24
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name与age
# print(stu.age)
print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过 _Student__age 进行访问
