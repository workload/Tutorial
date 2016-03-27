import win32com.client
import pythoncom

def POINT(x,y,z):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x,y,z))  

acad = win32com.client.Dispatch("AutoCAD.Application")  
doc = acad.ActiveDocument  
ms = doc.ModelSpace  
files = r"C:\Users\TOM\Desktop\02python\516.00-501.50.dwg"
doc.Utility.Prompt("hello World\n")
pt1= POINT(0.0,0.0,0.0)
ms.InsertBlock(pt1, files, 1.0,1.0,1.0, 0)


##############################################
import os
import win32com.client
import pythoncom

def getFileList(rootdir):   
    files = []
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字    
        for filename in filenames:                        #输出文件信息
            files.append(parent + "\\" + filename)    #输出文件路径信息       
    return files  

def POINT(x,y,z):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x,y,z)) 

if __name__ == "__main__":
    rootdir = r"C:\Users\TOM/Desktop\files"
    acad = win32com.client.Dispatch("AutoCAD.Application")  
    doc = acad.ActiveDocument  
    ms = doc.ModelSpace   
    pt1= POINT(0.0,0.0,0.0)    
    for fl in getFileList(rootdir):
        ms.InsertBlock(pt1, fl, 1.0,1.0,1.0, 0)
        print "%s is inserted" % fl
    print "all inserted!"
