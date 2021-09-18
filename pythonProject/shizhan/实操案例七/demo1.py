#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/13 21:32
constellation = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']

nature = ['有一种让人看见就觉得开心的感觉，阳光、乐观、坚强，性格直来直去，就是有点小脾气。',
          '很保守，喜欢稳定，一旦有什么变动就会觉得心里不踏实，性格比较慢热，是个理财高手。',
          '喜欢追求新鲜感，有点小聪明，耐心不够，因你的可爱性格会让很多人喜欢和你做朋友。',
          '情绪容易敏感，缺乏安全感，做事情有坚持到底的毅力，为人重情重义，对朋友和家人特别忠实。',
          '有着远大的理想，总想靠自己的努力成为人上人，总是期待被仰慕被崇拜的感觉。',
          '坚持追求自己的完美主义者。',
          '追求平等、和谐，交际能力强，因此朋友较多。最大的缺点就是面对选择总是犹豫不决。',
          '精力旺盛，占有欲强，对于生活很有目标，不达目的誓不罢休，复仇心重。',
          '崇尚自由，勇敢、果断、独立，身上有一股勇往直前的劲儿，只要想做，就能做。',
          '是最有耐心的，做事最小心。做事脚踏实地，比较固执，不达目的不罢休，而且非常勤奋。',
          '人很聪明，最大的特点是创新，追求独一无二的生活，个人主义色彩很浓重的星座。',
          '集所有星座的优缺点于一身。最大的优点是有一颗善良的心，愿意帮助别人。']

# 将两个列表转成集合
d = dict(zip(constellation, nature))
print(d)
key = input('请输入您的星座:')
flag = True
for item in d:
    if key == item:
        flag = True
        print(key, '的性格特点为:', d.get(key))
        break
    else:
        flag = False

if not flag:
    print('对不起，您输入有误')
