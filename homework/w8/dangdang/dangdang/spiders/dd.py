# -*- coding: utf-8 -*-
import scrapy
import chardet
from dangdang.items import DangdangItem

import requests

url = 'https://category.dangdang.com/pg1-cp01.54.00.00.00.00.html'
response = requests.get(url)
print(response.encoding)


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = [
        f'https://category.dangdang.com/pg{i}-cp01.54.00.00.00.00.html' for i in range(1, 6)]

    def parse(self, response):

        encoding = chardet.detect(response.body)['encoding']

        try:
            decoded_body = response.body.decode(encoding, errors='replace')
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
            decoded_body = ''

        filename = "computerScienceBooks.html"

        open(filename, 'w').write(decoded_body)

        books = response.xpath('//ul[@class="bigimg"]//li')

        items = []

        for book in books:
            item = DangdangItem()

            title = book.xpath('.//p[@class="name"]/a/text()').get()

            short_title = book.xpath('.//a[@class="pic"]/@title').get()
            
            author = book.xpath(
                './/p[@class="search_book_author"]/span/a/text()').get()
            
            now_price = book.xpath(
                './/p[@class="price"]/span[@class="search_now_price"]/text()').get()
            
            pre_price = book.xpath(
                './/p[@class="price"]/span[@class="search_pre_price"]/text()').get()
            
            item['title'] = title
            item['author'] = author
            item['now_price'] = now_price
            item['short_title'] = short_title
            item['pre_price'] = pre_price

            items.append(item)

        return items

# 在dangdang/dangdang 目录下运行 scrapy crawl dd -o computerScienceBooks.csv