# -*- coding: utf-8 -*-
import scrapy

class TagWebassemblySpider(scrapy.Spider):
    name = "tag-webassembly"
    start_urls = [
        'https://medium.com/tag/webassembly/latest',
    ]

    def parse(self, response):
        for item in response.css(".streamItem"):
            if item.css(".section-content h3::text").extract_first():
                yield {
                    'title': item.css(".section-content h3::text").extract_first(),
                    'text': item.css(".section-inner::text").extract_first(),
                    'datetime': item.css(".postMetaInline time::attr(datatime)").extract_first(),
                    'link': item.css(".postArticle-readMore>a::attr(href)").extract_first().split("?")[0],
                    'author_name': item.css(".postMetaInline-authorLockup>a::attr(href)").extract_first().split("?")[0],
                }