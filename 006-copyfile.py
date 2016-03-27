import os 
import shutil

def getFileList(rootdir):   
    files = []
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字    
        for filename in filenames:                        #输出文件信息
            files.append(filename) #输出文件路径信息       
    return files

def checklst():
    file = open(r"C:\Users\TOM\Documents\002pybookcode\00bgPython\map_csv3.csv","r")
    lst = []
    for line in file.readlines():
        line=line.strip('\n')
        lst.append(line)
    return lst

if __name__ == '__main__':
    outdir1 = "G:/choose1000"
    outdir2 = "G:/choose500"
    rootdir1 = "G:/1000"  
    rootdir2 = "G:/500" 
    for fls in getFileList(rootdir1):
        if fls in checklst():
            shutil.copyfile(rootdir1 + '/' + fls, outdir1 + '/' + fls)
            print "copy " + fls + " successful"
    print "1000比例尺 copy finished!"
    
    for fls in getFileList(rootdir2):
        if fls in checklst():
            shutil.copyfile(rootdir2 + '/' + fls, outdir2 + '/' + fls)
            print "copy " + fls + " successful"
    print "500比例尺 copy finished!"
