#Param(
#    [string]$argument
#)

[String] $TypeLanceur = "Production des Stoxks Mensueldebutmois"
Write-Host $TypeLanceur

try {
    [String] $currentDirPath = [System.IO.Path]::GetDirectoryName($PSCommandPath)
    [String] $modulesPath    = [System.IO.Path]::Combine([System.IO.Directory]::GetParent($currentDirPath), "modules")

    Import-Module ([System.IO.Path]::Combine($modulesPath, "common.psm1")) -DisableNameChecking

	$RetourCmdLine = ExecuteCmdLine $TypeLanceur $argument 
	
	Write-Host " "
	Write-Host "Code Sortie : $RetourCmdLine"

    exit $RetourCmdLine
}
catch
{
    Write-Host "CATCH erreur dans $PSCommandPath"
    [string] $sInvocationInfo = $_.Exception.ErrorRecord.InvocationInfo | SELECT PSCommandPath,ScriptLineNumber,OffsetInLine,Line |format-list -force| out-string
    [string] $sException = $_.Exception | SELECT CommandName,Message,StackTrace |format-list -force| out-string
    Write-Host "$sException $sInvocationInfo" -ForegroundColor Red

    exit -2
}
