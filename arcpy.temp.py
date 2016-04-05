import arcpy
arcpy.env.workspace = r"F:\file\poly_out2011.gdb"
for fc in arcpy.ListFeatureClasses():
    fields = 'landuse2011'
    with arcpy.da.UpdateCursor(fc, fields) as cursor:
        for row in cursor:
            row[0] = fc
            cursor.updateRow(row)
print "finished!"
