#Param(
#    [string]$argument
#)

Write-Host  Args[0] $Args[0]
Write-Host  Args[1] $Args[1]
Write-Host  Args[2] $Args[2]
[String] $argument="{'Moteur': '" + $Args[0] + "', 'Periodicite': '" + $Args[1] + "', 'Periode': '" + $Args[2] + "'}"
Write-Host "argument : $argument"

try {
    $currentDirPath = [System.IO.Path]::GetDirectoryName($PSCommandPath)
    $sParentPath = [System.IO.Directory]::GetParent($currentDirPath).parent.FullName.ToString()
    $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_unitaire.py"))

    $params = "-x -i 0 python.exe `"" + $PathLanceur + "`" `"" + $argument + "`""

    [string] $cmd =  "& `"C:\JmsAgent\bin\psexec.exe`" $params"
    Write-Host "$cmd"
    $Output = (Invoke-Expression $cmd) *>&1

    $Output | Write-Host

    Write-Host "exit : $LASTEXITCODE"

    exit $LASTEXITCODE
}
catch
{
    Write-Host "CATCH erreur dans $PSCommandPath"
    [string] $sInvocationInfo = $_.Exception.ErrorRecord.InvocationInfo | SELECT PSCommandPath,ScriptLineNumber,OffsetInLine,Line |format-list -force| out-string
    [string] $sException = $_.Exception | SELECT CommandName,Message,StackTrace |format-list -force| out-string
    Write-Host "$sException $sInvocationInfo" -ForegroundColor Red

    exit -2
}
