from pyautocad import Autocad, APoint
acad = Autocad(create_if_not_exists=True)
lys = acad.doc
l = lys.Layers("DLSS")
lys.ActiveLayer = lys.Layers("0")
for obj in lys.Modelspace:
    if obj.Layer == "DLSS":
        obj.delete()
l.delete()
lys.regen

#-----------------------------------------------------------------
from pyautocad import Autocad, APoint

acad = Autocad()
doc = acad.Application.Documents.Open(r'C:\Users\Administrator\Desktop\DX2\510.50-500.50.dwg')
l = doc.Layers("SUB")
doc.ActiveLayer = doc.Layers("0")
for obj in doc.Modelspace:
    if obj.Layer == "SUB":
        obj.delete()
l.delete()
doc.regen
