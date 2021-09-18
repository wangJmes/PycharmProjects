#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/13 21:55
dict_ticket = {'G1569': ['北京南-天津南', '18:05', '18:39', '00:34'],
               'G1567': ['北京南-天津南', '18:15', '18:49', '00:34'],
               'G8917': ['北京南-天津南', '18:20', '19:19', '00:59'],
               'G203': ['北京南-天津南', '18:35', '19:09', '00:34'],
               }
print('车次\t\t\t', '出发站-到达站\t', '出发时间\t\t', '到达时间\t\t', '历时')
for key in dict_ticket:
    print(key, end='\t\t')
    for item in dict_ticket.get(key):
        print(item, end='\t\t')
    print()  # 换行
train_number = input('请输入要购买的车次:')
client = input('请输入乘车人，如果是多人请使用逗号分隔:')
print(f'您已经购买了{train_number}次列车,{dict_ticket.get(train_number)[0]}{dict_ticket.get(train_number)[1]}开,',
      f'请{client}尽快换取纸质车票。 【铁路客服】')
