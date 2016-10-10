# -*- coding:utf-8 -*- 
from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def towrite(contentdict):
	f.writelines(unicode(contentdict['topic_reply_time']) + ',' +str(contentdict['topic_reply_content']) + ',' + unicode(contentdict['user_name']) + '\n')
def spider(url):
	html = requests.get(url)
	selector = etree.HTML(html.text)
	content_field = selector.xpath('//div[@class="list rel"]')
	item = {}
	for each in content_field:
		try:
			name = each.xpath('dl/dd/ul/li[3]/text()')[0]
		except:
			name = "no data"
		finally:   
			print name    
		try:   
			price = each.xpath('div/p/span[1]/text()')[0]
		except:
			price = "no data"
		finally:   
			print price        
		try:
			date = each.xpath('dl/dd/p[1]/a/text()')[0]
		except:
			date = "no data"     
		finally:   
			print date		
	    
		item['user_name'] = name
		item['topic_reply_content'] = price
		item['topic_reply_time'] = date
		towrite(item)

if __name__ == '__main__':
	pool = ThreadPool(8)
	f = open('content2.csv','a')
	page = []
	for i in range(1,73):
		newpage = 'http://esf.cd.fang.com/housing/132__0_0_0_0_'+ str(i) +'_0_0/'
		page.append(newpage)

	#for pg in page:
	 	#spider(pg)
	results = pool.map(spider, page)
	pool.close()
	pool.join()
	f.close()


