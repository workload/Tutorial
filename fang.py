# -*- coding:utf-8 -*- 
from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree
import logging
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GetListPage(object):
	def __init__(self,city_abbr):
		self.city_abbr = city_abbr

	def getUrl_multiTry(url):    #重复多少获取网页HTML
	    maxTryNum=10  
	    for tries in range(maxTryNum):  
		try:  
		    html2 = requests.get(url)  
		    break  
		except:  
		    if tries <(maxTryNum-1):  
			continue  
		    else:  
			logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
			break              
	    return html2


	def get_region(self):   #获取各个城市分地区小区列表第一页，共20个小区
	    region_url = []
	    url = "http://esf." + self.city_abbr[:-1] + ".fang.com/housing/__1_0_0_0_1_0_0/"
	    html = self.getUrl_multiTry(url)
	    selector = etree.HTML(html.text)
	    try:
		content_field = selector.xpath('//*[@id="SQinfo"]/div[@class="sq-info mt10"]/a/@href')
		for co in content_field:
		    url_region = "http://esf." + self.city_abbr[:-1] + ".fang.com" + co
		    region_url.append(url_region)
	    except:
			pass
	    return region_url



class WriteData(object):
	def __init__(self,f):
		self.f = f

	def getUrl_multiTry(url):    #重复多少获取网页HTML
	    maxTryNum=10  
	    for tries in range(maxTryNum):  
		try:  
		    html2 = requests.get(url)  
		    break  
		except:  
		    if tries <(maxTryNum-1):  
			continue  
		    else:  
			logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
			break              
	    return html2

	def towrite(contentdict):   #写入小区信息
	    self.f.writelines(unicode(contentdict['topic_reply_time']) + ',' +str(contentdict['topic_reply_content']) + ',' + unicode(contentdict['user_name']) + '\n')
	def spider(url):            #获取小区信息
	    html = self.getUrl_multiTry(url)
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
		self.towrite(item)




if __name__ == '__main__':
    #pool = ThreadPool(4)
    def get_page(url):	    #获取列表的页码
   	try:
	    html = requests.get(url)
	    selector = etree.HTML(html.text)
	    content_field = selector.xpath('//*[@id="houselist_B08_04"]/span/span/text()')[0]
	    return int(content_field[2:])
	except:
	    return 1

    city_path = r"h:\soufang\fang_city_use1.txt"
    open_city = open(city_path,"r")       # 打开城市缩写文件  
    lines = open_city.readlines()         #读取城市缩写内容
    open_city.close() 
    
    for city_abbr in lines:
		file= 'h:/soufang/' + city_abbr[:-1] +'.csv'
		file_open = open(f,'a')
		writedata = WriteData(file_open)
		list_all = GetListPage(city_abbr[:-1])

		page = []		
		for url_use in list_all.get_region():
		    try:
		    	page_count = get_page(url_use)
		    except:
		    	page_count = 1
			
		    for i in range(1,get_page(url_use)+1):
				newpage = url_use[:-6]+ str(i) +'_0_0/'
				page.append(newpage)

		for pg in page:
		    writedata.spider(pg)
	# results = pool.map(spider, page)
	#pool.close()
	#pool.join()
		f.close()
