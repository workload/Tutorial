# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

org_file=open(r"G:/baidu_csv.csv")       # 打开提取内容所在文件  
lines=org_file.readlines()                    #读取内容  
org_file.close()                                       #关闭以读取过的文件  
go_rep=open(r"G:\service_rep2.csv","a") 

def get_pre2char():
    org_new = []
    org_new2 = []
    for i in lines:
        if i[0:6] not in org_new:
            org_new.append(i[0:6])
            org_new2.append(i)
        else:
            pass            
    return org_new2 
   
if __name__ == "__main__":
    for line2 in get_pre2char():
        go_rep.write(line2)    
    exit()  
    go_rep.close() 
