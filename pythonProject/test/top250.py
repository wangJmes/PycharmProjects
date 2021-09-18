import requests
import bs4


def open_url(url):
    # 使用代理
    # proxies = {"http://127.0.0.1:1080", "http://127.0.0.2:1080"}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/85.0.4183.102 Safari/537.36'}

    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res


# 找出该网址一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next'). \
        previous_sibling.previous_sibling.text

    return int(depth)


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # 电影名
    movies = []
    targets = soup.find_all('div', class_='hd')
    for each in targets:
        movies.append(each.a.span.text)

    # 评分
    ranks = []
    targets = soup.find_all('span', class_='rating_num')
    for each in targets:
        ranks.append('评分：%s' % each.text)

    # 资料
    messages = []
    targets = soup.find_all('div', class_='bd')
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + \
                            each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + messages[i] + '\n')

    return result


def main():
    host = 'https://movie.douban.com/top250'
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?starts=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    # 保存电影信息
    with open("豆瓣TOP250电影.txt", 'w', encoding='utf-8') as f:
        for each in result:
            f.write(each)


if __name__ == "__main__":
    main()
