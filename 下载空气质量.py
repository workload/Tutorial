import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('gbk')

def getFrame(city):
    url = 'http://www.tianqihoubao.com/aqi/' + city +'.html'
    res = requests.get(url)
    html = res.text
    bf = BeautifulSoup(html)
    bf2 = bf.select('html')[0]
    bf3 = bf2.select('td')
    ls = []
    for i in bf3:
        ls.append(i.text.strip())    
    arr = np.array(ls)
    arr =arr.reshape(len(ls)/8,8)
    df =pd.DataFrame(arr)
    df.to_csv('C:\\Users\\TOM\\Desktop\\jupup\\mp2_5\\' + city +'.csv')
    print(city + 'finished!') 
if __name__ == '__main__':
    df =pd.read_csv(r'C:\Users\TOM\Desktop\jupup\city2.csv',encoding='gbk')
    for city in df['url']:
        getFrame(city)



################################################

import os

def getFileList(rootdir):   
    files = []
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字    
        for filename in filenames:                        #输出文件信息
            files.append(parent+"/"+filename) #输出文件路径信息       
    return files 

if __name__ == "__main__":
    rootdir = 'C:/Users/TOM/Desktop/jupup/mp2_5'
    flist = getFileList(rootdir)
    #要写入的文件
    ofile = open('C:/Users/TOM/Desktop/jupup/all_city.csv', 'a')
    #遍历读取所有文件，并写入到输出文件
    for fr in flist:
        for txt in open(fr, 'r'):
            ofile.write(txt)
    ofile.close()
    
