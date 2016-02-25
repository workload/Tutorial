# -*- coding: utf-8 -*-
import arcpy
import os
import urllib


def directionChoose(a,b):    #定义函数，实现图片下载
    #picture1    
    picture1 = arcpy.mapping.ListLayoutElements(mxd,"PICTURE_ELEMENT","picture1")[0]
    picture1caption = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","picture1caption")[0]
    heading = a
    picture1caption.text = "方向{0}度".format(heading)
    #调用百度街景API,具体参数见http://lbsyun.baidu.com/index.php?title=viewstatic/api
    url = "http://api.map.baidu.com/panorama/v2?ak=<API>&width=1024&height=512&location={0},{1}&heading={2}&pitch=15&fov=180 ".format(picLat,picLong,heading)
    picturePath = os.path.join(path,"%s1.jpg" % row[2])
    urllib.urlretrieve(url,picturePath)
    picture1.sourceImage = picturePath
   
    #picture2
    picture2 = arcpy.mapping.ListLayoutElements(mxd,"PICTURE_ELEMENT","picture2")[0]
    picture2caption = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","picture2caption")[0]
    heading = b
    picture2caption.text = "方向{0}度".format(heading)
    url = "http://api.map.baidu.com/panorama/v2?ak=<API>&width=1024&height=512&location={0},{1}&heading={2}&pitch=15&fov=180 ".format(picLat,picLong,heading)
    picturePath = os.path.join(path,"%s2.jpg" % row[2])
    urllib.urlretrieve(url,picturePath)
    picture2.sourceImage = picturePath
        
path = r"C:\Downloads\2016tuto"                      
mxdPath = os.path.join(path,"suzhou_sip.mxd")           
mxd = arcpy.mapping.MapDocument(mxdPath)                      
df = arcpy.mapping.ListDataFrames(mxd)[0]
geocodedAddressLayer = arcpy.mapping.ListLayers(mxd,"address",df)[0]

fieldsToRetrieve = ["OBJECTID","SHAPE@","street","city","province","direction"]
with arcpy.da.SearchCursor(geocodedAddressLayer,fieldsToRetrieve) as sc:
    pdfpaths = [] #创建一个空列表，用于后边存储导出PDF的地址
    for row in sc:
        df.extent = row[1].extent  
        df.scale = 1500    #地图的比例
        title = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "Title")[0]
        title.text = "%d.%s %s%s" % (row[0],row[2],row[4],row[3])
        picLat = row[1].firstPoint.X
        picLong = row[1].firstPoint.Y
       
        #自行增加调用函数，如道路方向有变，则角度进行相应调整即可
        if row[5] == "EW180":
            directionChoose(0, 180)
        else:                              
            directionChoose(90, 270)
        
        #下载各个PDF文档
        arcpy.mapping.ExportToPDF(mxd,os.path.join(path,"%s%s.pdf" % (row[3],row[2])))
        pdfpaths.append(os.path.join(path,"%s%s.pdf" % (row[3],row[2])))   #这里讲下载的PDF的地址添加进空列表
    pdfaps = r"C:\Downloads\2016tuto\suzhou_sip.pdf"  #创建一个合并后的PDF文档名称
    if os.path.exists(pdfaps):  #判断合并后的PDF文档名称是否存在，这个必须要。
        os.remove(pdfaps)
    pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfaps)
    for pdfpath in pdfpaths:    
        pdfDoc.appendPages(pdfpath)    #循环每一个PDF文档，并将其合并
    pdfDoc.saveAndClose()
    del pdfDoc


