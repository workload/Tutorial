import arcpy

fc = r'F:\001arcgisDocuments\2016zjg\zjgdoc.gdb\jingang_listnumb'
class_field = 'TextString'
with arcpy.da.SearchCursor(fc, class_field) as cursor:
    for row in cursor:
        doc = open('map_csv.csv','a') 
        if row[0].startswith('5'):          
            doc.write(row[0])
            doc.write('\n')
        doc.close            
