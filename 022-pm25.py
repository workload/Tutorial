# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree

def get_city_ls(url):
    res = requests.get(url)
    html = res.text
    res = etree.HTML(html)
    bf1 = res.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "citychk", " " ))]//a/@href')
    city_ls = list(set(bf1))
    return city_ls

def download_pm25(city_ls,path):
    file = open(path,'a')
    file.writelines("监测点"+","+"AQI指数"+","+"空气质量状况"+","+"PM2.5"+","+"PM10"+","+"Co"+","+"No2"+","+"So2"+","+"O3"+"\n")       
    for city in city_ls:
        city_url = "http://www.tianqihoubao.com" + city
        #print city_url
        res = requests.get(city_url)
        html = res.text
        res = etree.HTML(html)
        tr = res.xpath('//td/text()')[9:]
        #print tr[0]
        ls = []
        for i in tr:
            data = i.strip()  
            ls.append(data+',')
        for i in range(0,len(ls)/9+1):       
            file.writelines(ls[i*9:i*9+9])
            file.writelines("\n")
    file.close()

if __name__ == "__main__":
    url = 'http://www.tianqihoubao.com/aqi'
    path =  r'E:\pm25_all_2.csv'
    lst = get_city_ls(url)
    download_pm25(lst,path)
     
