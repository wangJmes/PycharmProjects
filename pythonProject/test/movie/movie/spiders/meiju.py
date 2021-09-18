import scrapy
from ..items import MovieItem


class MeijuSpider(scrapy.Spider):  # 继承这个类
    name = 'meiju'  # 名字
    allowed_domains = ['meijutt.tv']  # 域名
    start_urls = ['https://www.meijutt.tv/new100.html']  # 要补充完整

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        # 意思是选中所有的属性class值为"top-list  fn-clear"的ul下的li标签内容
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item  # 一种特殊的循环
