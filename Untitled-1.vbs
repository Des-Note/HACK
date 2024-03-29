' Spécifiez le chemin du répertoire où vous voulez créer les dossiers
strDirectory = "C:\Users\narut\Desktop\dossier infini"

' Nombre de dossiers à créer
Const nombreDossiers = 1000

' Création des dossiers
For i = 1 To nombreDossiers
    nomDossier = "Dossier_" & i
    cheminDossier = strDirectory & "\" & nomDossier
    
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    If Not objFSO.FolderExists(cheminDossier) Then
        objFSO.CreateFolder(cheminDossier)
    End If
Next
