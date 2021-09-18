# -*- coding: utf-8 -*-

"""
--------------------------------------------------------
# @Version : python3.7
# @Author  : wangTongGen
# @File    : main.py
# @Software: PyCharm
# @Time    : 2019/1/8 21:25
--------------------------------------------------------
# @Description:
--------------------------------------------------------
"""

import os
import re
import json
import requests


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36 '
    }

    path = './results/imgs'
    if not os.path.exists(path):
        os.makedirs(path)

    url = 'https://maoyan.com/board/4?offset={}'
    for i in range(0, 100, 10):

        items = get_one_page(url.format(str(i)), headers)
        for item in items:
            print(item)
            write2txt(item, './results/result.txt')
            save_imgs(item, headers)


def save_imgs(item, headers):
    response = requests.get(item['img_url'], headers=headers).content

    with open('./results/imgs/' + item['rank'] + '_' + item['title'] + '.jpg', 'wb') as f:
        f.write(response)


def write2txt(item, save_path):
    with open(save_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False, indent=2) + '\n')


def get_one_page(url, headers):
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()

    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)<.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>('
        '.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html_str)

    for item in items:
        yield {
            'rank': item[0],  # 排名
            'img_url': item[1],  # 图片链接
            'title': item[2],  # 电影名字
            'actors': item[3].strip(),  # 主演
            'date': item[4],  # 上映时间
            'score': item[5] + item[6]  # 评分
        }


if __name__ == '__main__':
    main()
