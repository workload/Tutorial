import array
import comtypes.client

#Get running instance of the AutoCAD application
app = comtypes.client.GetActiveObject("AutoCAD.Application")

#Get the ModelSpace object
ms = app.ActiveDocument.ModelSpace

#Add a POINT in ModelSpace
pt = array.array('d', [0,0,0])
point = ms.AddPoint(pt)

#Add a LINE in ModelSpace
pt1 = array.array('d', [1.0,1.0,0])
pt2 = array.array('d', [2.0,2.0,0])
line = ms.AddLine(pt1, pt2)

#Add an integer type xdata to the point.
point.SetXData(array.array("h", [1001, 1070]), ['Test_Application1', 600])

#Add a double type xdata to the line.
line.SetXData(array.array("h", [1001, 1040]), ['Test_Application2', 132.65])

#Add a string type xdata to the line.
line.SetXData(array.array("h", [1001, 1000]), ['Test_Application3', 'TestData'])

#Add a list type (a point coordinate in this case) xdata to the line.
line.SetXData(array.array("h", [1001, 1010]),
              ['Test_Application4', array.array('d', [2.0,0,0])])

print "Done."
