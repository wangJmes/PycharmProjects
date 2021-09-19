# 练习
# 开发者:汪川
# 开发时间: 2021/8/26 15:36
import schedule
import time


def job():
    print('哈哈------')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
