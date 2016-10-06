# -*- coding:utf-8 -*-
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def getUrl_multiTry(url):  
    user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
    headers = { 'User-Agent' : user_agent }  
    maxTryNum=10  
    for tries in range(maxTryNum):  
        try:  
            req = urllib2.Request(url, headers = headers)   
            html=urllib2.urlopen(req).read()  
            break  
        except:  
            if tries <(maxTryNum-1):  
                continue  
            else:  
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
                break              
    return html
if __name__ == "__main__":
    url = "http://www.fang.com/SoufunFamily.htm"
    html = getUrl_multiTry(url)
    choice = r'<a href="http://(.*?).fang.com/" target.*?>(.*?)</a>'
    res = re.compile(choice)
    numbers = re.findall(choice,html)
    go_rep=open(r"G:\fang2.csv","a") 
    for num in numbers:
        lists = num[0]+','+num[1]
        go_rep.write(lists+'\n')    
    print "数据全部录入！"
    exit()  
    go_rep.close() 
    
