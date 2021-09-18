#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/16 12:09
class Car:
    def __init__(self, type, no):
        self.type = type
        self.no = no

    def start(self):
        pass

    def stop(self):
        pass


class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company

    def start(self):
        print('乘客您好')
        print(f'我是{self.company}出租车公司的，我的车牌是{self.no},请问您要去哪里？')

    def stop(self):
        print('目的地到了，请您付款下车，欢迎在此乘坐')


class FamilyCar(Car):
    def __init__(self, type, no, name):
        super().__init__(type, no)
        self.name = name

    def stop(self):
        print('目的地到了，我们去玩儿吧')

    def start(self):
        print(f'我是{self.name},我的汽车我做主')


if __name__ == '__main__':
    taxi = Taxi('上海大众', '京A97658', '长城')
    taxi.start()
    taxi.stop()
    family = FamilyCar('北京现代', '苏NN466N', '车主')
    family.start()
    family.stop()
