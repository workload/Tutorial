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
