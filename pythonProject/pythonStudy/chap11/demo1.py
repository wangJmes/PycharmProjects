# 练习
# 开发者:汪川
# 开发时间: 2021/5/2 17:28
import traceback

try:
    print('------------')
    print(1 / 0)
except:
    traceback.print_exc()
