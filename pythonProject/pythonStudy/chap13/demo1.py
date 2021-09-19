# 练习
# 开发者:汪川
# 开发时间: 2021/8/23 16:19
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')


car = Car('宝马X5')
car.start()
print(car.brand)
