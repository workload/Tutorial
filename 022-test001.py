# -*- coding:utf-8 -*-
import arcpy
from pyautocad import Autocad

def fcOut(fc, field):
    with arcpy.da.SearchCursor(fc, field) as cursor:
        ls = [ls[0] for ls in cursor]
        ls2 = list(set(ls))
        for i in ls2:
            out_fc = db_out + '/' + i
            arcpy.Select_analysis(fc, out_fc, field + "= '" + i + "'")    
        
def fc2dwg(dwgname):        
    in_features = arcpy.ListFeatureClasses()
    output_type = "DWG_R2007"
    output_file = 'F:/file/' + dwgname
    arcpy.ExportCAD_conversion(in_features, output_type, output_file)

def hatchCAD(dwg):
    acad = Autocad()
    doc = acad.Application.Documents.Open(dwg)         
    patternName = "SOLID"
    PatternType = 0
    bAssociativity = True  
    try:
        doc.ActiveLayer = doc.Layers("0")
        for obj in doc.Modelspace:
            if obj.Layer == "A1(行政办公用地)":
                obj.layer.Truecolor = 231
                hatchobj = obj.AddHatch(PatternType, patternName, bAssociativity)
                outerloop = obj.layer("A1(行政办公用地)")
                hatchobj.AppendOuterLoop(outerloop)
                hatchobj.Evaluate
            elif obj.Layer == "A2(文化设施用地)":
                obj.layer.Truecolor = 241
                hatchobj = obj.AddHatch(PatternType, patternName, bAssociativity)
                outerloop = obj.layer("A2(文化设施用地)")
                hatchobj.AppendOuterLoop(outerloop)
                hatchobj.Evaluate                










































































































































































            elif obj.Layer == "G2(防护绿地)":
                obj.layer.Truecolor = 94
                hatchobj = obj.AddHatch(PatternType, patternName, bAssociativity)
                outerloop = obj.layer("G2(防护绿地)")
                hatchobj.AppendOuterLoop(outerloop)
                hatchobj.Evaluate  
            elif obj.Layer == "G3(广场用地)":
                obj.layer.Truecolor = 93
                hatchobj = obj.AddHatch(PatternType, patternName, bAssociativity)
                outerloop = obj.layer("G3(广场用地)")
                hatchobj.AppendOuterLoop(outerloop)
                hatchobj.Evaluate
            else:
                pass
    except:            
        print u"%s填充不成功，请检查" % obj.name
    finally:
        doc.save()
        doc.close()

if __name__ == "__main__":    
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace =  "F:/file/db_out.gdb"
    db_out = arcpy.env.workspace
    fc = "F:/file/db_in.gdb/landuse_2015"     
    field = "LB"                                    
    dwgname = "landuse2015.dwg"
    fcOut(fc,field)
    fc2dwg(dwgname)
    hatchCAD('F:/file/' + dwgname)
    print "finished!"
