# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem
import lxml

class AlibabapositionSpider(scrapy.Spider):
    name = 'Alibabaposition'
    allowed_domains = ['campus.alibaba.com']
    start_urls = ['https://campus.alibaba.com/traineePositionList']

    def parse(self, response):
        alibaba_position = response.xpath("//div/div/table//tr[@data-type ='11']")
        item = TencentItem()
        i = 1
        for each in alibaba_position:
            position = each.xpath('./th/a/text()').extract()
            # 获取职位具体工作岗位
            information = each.xpath('./td/text()').extract()

            # techlogy =each.xpath('./td[@data-spm-anchor-id="0.0.0.i%s.1672725fHqSMuq"]/text()'%i).extract()
            # i += 1
            techlogy = each.xpath('./td/text()').extract()
            # 获取工作城市

            work_city =each.xpath('./td[@class="work-city"]/text()').extract()
            # 获取毕业时间
            # generation =each.xpath('./td[@data-spm-anchor-id="0.0.0.i%s.1672725fHqSMuq"]/text()'%i).extract()
            # i += 1
                # 获取职位具体信息
            detail = each.xpath('./td[@class="position-detail"]/a/text()').extract()

            item['position'] = position[0]
            item['techlogy'] = techlogy[0]
            item['work_city'] = work_city[0]
            item['generation'] = techlogy[1]
            item['detail'] = detail[0]

            yield item





