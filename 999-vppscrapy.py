# -*- coding: utf-8 -*-
# 
#
import scrapy

from apple.items import AppleItem as DmozItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import  LinkExtractor
from bs4 import BeautifulSoup
from lxml import etree
import re
class DmozSpider(CrawlSpider):
     name = "dmoz55"
     area_code = '5255'
     start_urls = ["http://esf.sh.fang.com/housing/_"+area_code+"_1_0_0_0_1_0_0/"
               ]
     rules = [
          Rule(LinkExtractor(allow='/housing/_'+area_code+'_1_0_0_0_\d{1,3}_0_0/'), callback='parse_list', follow=True)

     ]
     

     def parse_list(self, response): #http://esf.sh.fang.com/housing/_5920_1_0_0_0_1_0_0/
          for sel in response.xpath('/html/body/div[4]/div[5]/div[4]/div'):
               # item = DmozItem()
               # item['name'] = sel.xpath('dl/dd/p[1]/a/text()').extract()[0]
               # item['price'] = sel.xpath('div/p[1]/span[1]/text()').extract()[0]
               url = sel.xpath('dl/dd/p[1]/a/@href').extract()[0]
               yield scrapy.Request(url, callback=self.parse_detail)


     def parse_detail(self, response):  #http://yijushangcheng.fang.com/
          item = DmozItem()
          item['name'] = response.xpath('//*[@id="esfbjxq_04"]/text()').extract()[0]    #[:-3]
          item['resd'] = response.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[2]/ul[descendant-or-self::text()]').extract()[0]

          url = response.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/a/@href').extract()[0]
          request = scrapy.Request(url,callback=self.parse_detail2)
          request.meta['item'] = item
          return request


     def parse_detail2(self, response):  #http://yijushangcheng.fang.com/xiangqing/
          item = response.meta['item'] 
          # item['name'] = response.xpath('/html/body/div[4]/div[2]/div[2]/h1/a/text()').extract()[0][:-3]
          # item['resd'] = response.xpath('/html/body/div[4]/div[4]/div[1]/div[2]/div[2]/dl[descendant-or-self::text()]').extract()[0]

          url = response.xpath('/html/body/div[4]/div[4]/div[1]/div[7]/div[2]/dt/iframe/@src').extract()[0]
          request = scrapy.Request(url,callback=self.parse_detail3)
          request.meta['item2'] = item
          return request

     def parse_detail3(self, response): #http://esf.sh.fang.com/newsecond/map/NewHouse/NewProjMap.aspx?newcode=1210593112
          item = response.meta['item2']       
          rr = response.xpath('/html/head/script[6][descendant-or-self::text()]').extract()[0]
          com = re.compile(r'px:"(.*?)",py:"(.*?)",isKey') 
          it = re.findall(com,rr)
          # item['coor_x'] = list(it[0])[0]
          # item['coor_y'] = list(it[0])[1]
          item['coor_x'] = it[0][0]
          item['coor_y'] = it[0][1]
          return item

