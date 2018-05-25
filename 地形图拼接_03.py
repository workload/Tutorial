# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------

import arcpy
import os
import time
arcpy.env.overwriteOutput = True


class select_num(object):
    def __init__(self,polygon_name,point_name,select_anno,sp_fc,final_fc):
        self.polygon_name = polygon_name
        self.point_name = point_name    
        self.select_anno = select_anno 
        self.sp_fc = sp_fc 
        self.final_fc = final_fc 
        
    def polygon(self):
        inFeatures1 = os.path.join(workspce, cad, cad_use[0])
        outFeatureClass = os.path.join(workspce, creat_gdb, self.polygon_name)
        arcpy.FeatureToPolygon_management(inFeatures1, outFeatureClass)
    
        inFeatures2 = os.path.join(workspce, cad, cad_use[1])
        outFeatureClass = os.path.join(workspce, creat_gdb, self.point_name)
        arcpy.FeatureToPoint_management(inFeatures2, outFeatureClass)
    
        where_clause = " RefName LIKE '5%' OR RefName LIKE '3%'"
        # 筛选符合要求的编号，其都以5和3开头
        select_fc = os.path.join(workspce, creat_gdb, self.select_anno)
        arcpy.Select_analysis(os.path.join(workspce, creat_gdb, self.point_name), select_fc , where_clause)

        outFeatureClass = os.path.join(workspce, creat_gdb, self.sp_fc)
        arcpy.SpatialJoin_analysis(os.path.join(workspce, creat_gdb, self.polygon_name), 
                                   os.path.join(workspce, creat_gdb, self.select_anno), 
                                   outFeatureClass)
        
        arcpy.MakeFeatureLayer_management(os.path.join(workspce, creat_gdb, self.sp_fc), "lyr")
        arcpy.SelectLayerByLocation_management ("lyr", select_features = area_fc)
        arcpy.CopyFeatures_management("lyr", os.path.join(workspce, creat_gdb, self.final_fc))

if __name__ == "__main__":   
    print "开始处理，请稍等..."
    workspce = r"G:\2016tuto"   # 工作空间
    cad = "总拼接表orh.dwg"      # 地形图拼接表
    creat_gdb = "dx.gdb"        # 创建用于存储临时文件的数据库空间 
    area_use = "tqfw"           # 这里单个区域的要素类，多个加for循环
    gdb2 = 'dxtpj.gdb'                    
    cad_use = ["Polyline", "annotation"]      # 地形图文件上图幅编号一般存在annotation中
    area_fc = os.path.join(workspce,gdb2,area_use)
    arcpy.CreateFileGDB_management(workspce, creat_gdb)
    
    start_time = time.time()                                                          
    process = select_num('a1','a2','a3','a4','a5')  
    process.polygon()
    
    fc = os.path.join(workspce, creat_gdb, 'a5')    
    class_field = 'RefName'
    with arcpy.da.SearchCursor(fc, class_field) as cursor:
        for row in cursor:
            doc = open(os.path.join(workspce, 'map_csv.csv'),'a')  # 如果多个文件，
            if row[0] is not None:          
                doc.write(row[0])
                doc.write('\n')
            doc.close
    print u"CSV文件生成！"     
    end_time = time.time()                                                              
    print "完毕，用时%.2f秒" % (end_time - start_time)
