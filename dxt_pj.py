import os
from pyautocad import Autocad, APoint
import arcpy

def checkID(town):
    fc = r'F:\[2016.03]张家港项目\地形图分镇拼接\地形图拼接.gdb' + town
    class_field = 'TextString'
    with arcpy.da.SearchCursor(fc, class_field) as cursor:   
        ls = [ls[0] for ls in cursor]
        ls2 = list(set(ls))
        ls3 = []
        for dxt in ls2:
            if dxt.startswith('5'):
                ls3.append(dxt.replace(" ",""))
        return ls3

def getFileList(dxt_dir):   
    files = []
    for parent,dirnames,filenames in os.walk(dxt_dir):     
        for filename in filenames:                       
            files.append(filename)
    return files

if __name__ == "__main__":
    towns = ['金港','杨舍','大新','乐余','塘桥','锦丰','凤凰','南丰','现代农业园']
    for town in towns:
        dxt_dir = r'C:\Users\Administrator\Desktop\DX2'
        acad = Autocad(create_if_not_exists=True)
        main_doc = acad.doc
        for file_use in getFileList(dxt_dir):
            if file_use in checkID(town):
                ms = main_doc.ModelSpace  
                file_to_insert = dxt_dir + '\\' + file
                pt1= POINT(0.0,0.0,0.0)
                ms.InsertBlock(pt1, file_to_insert, 1.0,1.0,1.0, 0)
                print "%s is inserted" % fl
            else:
                pass
        main_doc.save()
        main_doc.close()
        print town + "finished!"
    print "all town finished"
