# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #获取职称
    position = scrapy.Field()
    #获取职位具体工作岗位
    techlogy = scrapy.Field()
    #获取工作城市
    work_city = scrapy.Field()
    #获取毕业时间
    generation = scrapy.Field()
    #获取职位具体信息
    detail = scrapy.Field()

