#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/17 21:23
def find_answer(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # if line=='' 到文件末尾退出
                break
            # 字符串分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False


if __name__ == '__main__':
    question = input('hi，您好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧:')
    while True:
        if question == 'bye':
            break
        else:
            # 开始在文件中查找
            replay = find_answer(question)
            if not replay:  # 如果回复的是False，
                question = input('小蜜不知道你在说什么，您可以问一些关于订单、物流、账户、支付等问题，（退出请输入bye）')
            else:
                print(replay)
                question = input('小主，您还可以继续问一些关于订单、物流、账户、支付等问题（退出请输bye）')
    print('小主再见')

