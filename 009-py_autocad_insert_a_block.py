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
