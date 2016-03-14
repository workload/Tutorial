Private Sub CommandButton11_Click()
   CommonDialog2.CancelError = True
   With CommonDialog2
          .Filter = "*.dwg|*.dwg"
          .ShowSave
          Dim A As String
          A = Trim(.FileName)
          i = InStrRev(A, "\")
          MyPath = Mid(A, 1, i)    ' 文件目录
   End With
   UserForm1.hide
     
   Dim MyFile, MyName As String
   MyFile = Dir(MyPath & "*.dwg")
   
   Do While MyFile <> ""   ' 开始循环。
        
        nextline = Trim(MyFile)
        
        gangwei = InStrRev(nextline, ".")

        MyName1 = Mid(nextline, 1, gangwei - 1)

        ThisDrawing.Application.Documents.Open MyPath & MyName1 & ".dwg"   '打开文件

   Dim layerexit As Boolean
   layerexit = False
   Dim MyLay As AcadLayer

    For Each MyLay In ThisDrawing.Layers        '判断图层是否存在
   If MyLay.Name = "TK" Then layerexit = True
   Next
    If layerexit Then
        DelAllInLayer ("TK")   '删除TK图层
    End If

        ThisDrawing.Application.Documents(MyName1 & ".dwg").Save        '保存文件
        ThisDrawing.Close
        MyFile = Dir
    Loop
End Sub


'删除图层函数
 Function DelAllInLayer(ByVal LName As String)
 '清除选择集
   On Error Resume Next
     Call ThisDrawing.SelectionSets("sssl").Delete
     On Error Resume Next

'创建选择集
        Dim SSet As AcadSelectionSet
        Set SSet = ThisDrawing.SelectionSets.Add("sssl")
        Dim ft(0) As Integer, Fd(0)
        ft(0) = 8: Fd(0) = LName      '要问ft(0)为什么是8，下面的选择函数里，ft(0)是DXF组码，你转出一个dxf，然后用记事本打开，就可以看出来，dxf里面，图层的组码就是8

'选中符合选择条件的元素，这个是选中指定图层名的所有元素
        SSet.Select acSelectionSetAll, , , ft, Fd
'循环删除选择集里每一个元素
        Dim E As AcadEntity
        For Each E In SSet
            E.Delete    '删除
        Next
   End Function

