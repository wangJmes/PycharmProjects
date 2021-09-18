# 练习
# 开发者:汪川
# 开发时间: 2021/5/20 21:47
# 练习
# 开发者:汪川
# 开发时间: 2021/5/20 21:03
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import time

url = 'https://movie.douban.com/typerank?type_name=爱情片&type=13&interval_id=100:90&action='
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/63.0.3239.132 Safari/537.36"')
browser = webdriver.Chrome()
browser.get(url)
wait = WebDriverWait(browser, 10)


def get_page():
    browser.implicitly_wait(10)
    for i in range(50):
        time.sleep(0.3)
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 下滑操作
        print('正在下滑第{}次'.format(i))
        print('-------------')
    # time.sleep(10)
    print("*****请等待几秒*****")
    time.sleep(10)
    when = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                           '#content > div > div.article > '
                                                           'div.movie-list-panel.pictext > div:nth-child(380) > div > '
                                                           'a > img')))
    # -----------------------------------------------------------------
    movies = browser.find_elements_by_class_name('movie-name-text')
    names = []
    for item in movies:
        if item.text != '':
            names.append(item.text)
    print("爬取成功")
    print(len(names))
    # ---------------------------------------------------------------
    playables = browser.find_elements_by_class_name('playable-sign')
    playable_sign = []
    for sign in playables:
        if sign.text != '':
            playable_sign.append(sign.text)
    print('爬取成功')
    print(len(playable_sign))
    # ------------------------------------------------------------
    rank_names = browser.find_elements_by_class_name('rank-num')
    ranks = []
    for rank in rank_names:
        if rank.text != '':
            ranks.append(rank.text)
    print('爬取成功')
    print(len(ranks))
    # ---------------------------------------------------------
    actors = browser.find_elements_by_class_name('movie-crew')
    actor_list = []
    for actor in actors:
        if actor.text != '':
            actor_list.append(actor.text)
    print('爬取成功')
    print(len(actor_list))
    # ----------------------------------------------------------
    clasic = browser.find_elements_by_class_name('movie-misc')
    miscs = []
    for misc in clasic:
        if misc.text != '':
            miscs.append(misc.text)
    print('爬取成功')
    print(len(miscs))
    # -----------------------------------------------------------
    rates = browser.find_elements_by_class_name('movie-rating')
    rate = []
    for score in rates:
        if score.text != '':
            rate.append(score.text)
    print('爬取成功')
    print(len(rate))
    # -----------------------------------------------------------
    '''
  links=browser.find_elements_by_class_name('movie-content')
  for link in links:
    link_img=link.get_attribute('data-original')
    print(link_img)
  '''
    return rate, miscs, actor_list, ranks, playable_sign, names


if __name__ == "__main__":
    rate, miscs, actor_list, ranks, playable_sign, names = get_page()
    datas = pd.DataFrame({'names': names, 'rank': ranks, '分类': miscs, '评分': rate})
    try:
        datas.to_csv('selenium_results\douban.csv', encoding='utf_8_sig')
        print("保存成功")
        print(datas)
    except:
        print('保存失败')
