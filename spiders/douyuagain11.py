# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuagainItem

class Douyuagain11Spider(scrapy.Spider):
    name = 'douyuagain12'
    allowed_domains = ['douyu.com']
    start_urls = ['https://www.douyu.com/gapi/rkc/directory/2_201/1']

    def parse(self, response):
        item = DouyuagainItem()
        data_list = json.loads(response.text)['data']['rl']
        for data in data_list[:2]:
            item['nickname'] = data['nn']
            item['img_url'] = data['rs1']
            yield item
        pass
