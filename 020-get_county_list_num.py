# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time



def get_countynum(city_code):
    url = 'http://esf.' + city_code + '.fang.com/housing'
    #html = urllib2.urlopen(url).read()
    html = requests.get(url).text
    choice = r'<a href="/housing/(\d{1,7})__0_0_0_0_1_0_0/">'
    res = re.compile(choice)
    numbers = re.findall(res,html)
    return numbers

if __name__ == "__main__":
    city_path = u"G:/003研究文件/lj/fang_city_use.csv"
    open_city = open(city_path,"r")       # 打开提取内容所在文件  
    lines=open_city.readlines()                #读取内容  
    open_city.close()  
    for line in lines:
        city_code = line.split(",")[0]
        #print 'http://esf.' + city_code + '.fang.com/housing'
        try:
            city_all_num = get_countynum(city_code)
            print city_code+',',city_all_num
            time.sleep = 3
            #for city_ls in city_all_num:
                #print city_ls
        except:
            print city_code+','+"no data!"
            time.sleep = 3
            
    print "数据全部录入！"
#go_rep=open(r"G:\fang2.csv","a") 
#for num in numbers:
    #lists = num[0]+','+num[1]
    #go_rep.write(lists+'\n')    
#print "数据全部录入！"
#exit()  
#go_rep.close() 
