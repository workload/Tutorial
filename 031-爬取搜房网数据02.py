# -*- coding:utf-8 -*- 
from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


url = "http://esf.sh.fang.com/housing/__1_0_0_0_1_0_0/"
html = requests.get(url)
selector = etree.HTML(html.text)
content_field = selector.xpath('//*[@id="SQinfo"]/div[@class="sq-info mt10"]/a/@href')
for co in content_field:
    print co
