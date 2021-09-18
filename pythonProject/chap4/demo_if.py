# 练习
# 开发者:汪川
# 开发时间: 2021/3/15 17:04
money = 1000  # 余额
s = int(input('请输入取款金额'))
#  判断余额是否充足
if money >= s:
    money -= s
    print('取款成功，余额为:', money)
