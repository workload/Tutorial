# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------

import arcpy
import os
import time
arcpy.env.overwriteOutput = True

print "开始处理，请稍等..."
start_time = time.time() 

workspce = r"G:\2016tuto"
cad = "总拼接表orh.dwg"
creat_gdb = "dx.gdb"
area_use = "tqfw"
gdb2 = 'dxtpj.gdb'
cad_use = ["Polyline", "annotation"]
area_fc = os.path.join(workspce,gdb2,area_use)

arcpy.CreateFileGDB_management(workspce, creat_gdb)   

polygon_name = 'polygon_name'
point_name = 'point_name'    
select_anno = 'select_anno' 
sp_fc = 'sp_fc' 
final_fc = 'final_fc' 

inFeatures = os.path.join(workspce, cad, cad_use[0])
outFeatureClass = os.path.join(workspce, creat_gdb, polygon_name)
arcpy.FeatureToPolygon_management(inFeatures, outFeatureClass)

inFeatures = os.path.join(workspce, cad, cad_use[1])
outFeatureClass = os.path.join(workspce, creat_gdb, point_name)
arcpy.FeatureToPoint_management(inFeatures, outFeatureClass)

where_clause = " RefName LIKE '5%' OR RefName LIKE '3%'"
select_fc = os.path.join(workspce, creat_gdb, select_anno)
arcpy.Select_analysis(os.path.join(workspce, creat_gdb, point_name), select_fc , where_clause)

outFeatureClass = os.path.join(workspce, creat_gdb, sp_fc)
arcpy.SpatialJoin_analysis(os.path.join(workspce, creat_gdb, polygon_name), 
                           os.path.join(workspce, creat_gdb, select_anno), 
                           outFeatureClass)

arcpy.MakeFeatureLayer_management(os.path.join(workspce, creat_gdb, sp_fc), "lyr")
arcpy.SelectLayerByLocation_management ("lyr", select_features = area_fc)
arcpy.CopyFeatures_management("lyr", os.path.join(workspce, creat_gdb, final_fc))

fc = os.path.join(workspce, creat_gdb, final_fc)
class_field = 'RefName'
with arcpy.da.SearchCursor(fc, class_field) as cursor:
    for row in cursor:
        doc = open(os.path.join(workspce, 'map_csv.csv'),'a') 
        if row[0] is not None:          
            doc.write(row[0])
            doc.write('\n')
        doc.close
print u"CSV文件生成！"    

end_time = time.time()
print "完毕，用时%.2f秒" % (end_time - start_time)
