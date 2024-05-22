#===================================================================
# Fonctions utilisées dans les traitements Python
#===================================================================
# Nom : common.psm1
#
#===================================================================

#===================================================================
# Parametres
#===================================================================


#===================================================================
# Fonctions
#===================================================================


<#  
.DESCRIPTION  
    Execute la ligne de commande passée en paramètre
		Construit la ligne de commande 
		Lance la commande. Recupération du flux OUT, pour en faire une pièce jointe du mail qui sera envoyé aux exploitants
		Teste le code retour de la commande
	
.PARAMETRES  
	[in] $hashParam					: Parametres généraux
	[in] $hashCMD					: Parametres spécifiques de la commande à executer
	[out]							:
	[ret]$boolTraitementEnErreur	: $true controle KO
	
.NOTES  
	Cette fonction n'envoie pas de mail
	
.LINK  
   
.EXAMPLE    
   
#>
function ExecuteCmdLine
{
	[CmdletBinding()]
	Param
	( 
		[Parameter(mandatory=$true,ValueFromPipeline=$true,Position = 0)] [String] $TypeLanceur,
        [Parameter(mandatory=$false,ValueFromPipeline=$true,Position = 1)] [String] $Arguments = $null
	)
  
	begin
	{
		
		[String] $strSource = "ExecuteCmdLine"

		Write-Host " "
		Write-Host "function "$strSource

        $currentDirPath = [System.IO.Path]::GetDirectoryName($PSCommandPath)
        $sParentPath = [System.IO.Directory]::GetParent($currentDirPath).parent.FullName.ToString()

        [String] $PathLanceur = [String]::Empty

        switch($TypeLanceur)
        {
            "Production des Moteurs Statistique" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_production.py"))
                break
            }
            "Production des Stoxks Mensueldebutmois" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_mensueldebutmois_stocks.py"))
                break
            }
            "Production Hebdo Recalcul SIG" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_hebdomadaire_historique.py"))
                break
            }
            "Relance des Moteurs Statistique" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_relance_moteurs.py"))
                break
            }
			"Relance des Ventes en Prescription Etrangeres" {
				$PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_relance_ventes.py"))
				break
			}
			"Relance des Sognow" {
				$PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_relance_sognow.py"))
				break
			}
            "Reprise sur Echec de la Production des Moteurs Statistique" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_reprise.py"))
                break
            }
            { $_ -in "Production Achats Calls", "Production Calls" } {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_unitaire.py"))
                break
            }
			"Depot Sognow" {
				$PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "moteur_statistique", "lanceur_depot_sognow.py"))
				break
			}
            "Production Etudes INDIC" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "etude", "lanceur_indic.py"))
                break
            }
            "Production Calls Ventes" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "calls", "lanceur_calls_ventes.py"))
                break
            }
            "Production Calls Achats" {
                $PathLanceur = ([System.IO.Path]::Combine($sParentPath, "script", "lanceurs", "calls", "lanceur_calls_achats.py"))
                break
            }
        }

        [String]  $cmdExe                   = "C:\JmsAgent\bin\psexec.exe"	
		[Boolean] $boolTraitementEnErreur 	= $false
        [Boolean] $boolVerbose              = $true
        [Boolean] $boolDebug                = $false
        [Boolean] $boolPrePROD              = $false
        [String]  $sPlateforme              = "RECETTE"
        [int32]   $ExecExitCode             = 0

        if([String]::IsNullOrEmpty($Arguments) -eq $false)
        {
            [String]  $cmdParams                = "-x -i 0 python.exe `"" + $PathLanceur + "`" `"" + $Arguments + "`""
        }
        else
        {
            [String]  $cmdParams                = "-x -i 0 python.exe `"" + $PathLanceur + "`""
        }
	} 
  
	Process 
	{
		try 
		{  	
            if([String]::IsNullOrEmpty($PathLanceur) -eq $true)
            {
                throw "Aucun lanceur n'est repertorie pour ce type de lanceur. On sort en erreur"
            }
            		
			if ( $boolVerbose -eq $true )
			{
				Write-Host Plateforme		: $sPlateforme
				Write-Host Commande Line	: $cmdExe
				Write-Host Parametres		: $cmdParams
			}
			
			[String] $CmdExecPath	= Resolve-Path $cmdExe				
			[String] $strParamCMD	= $cmdParams

			Write-Host " "
			Write-Host "On va executer "$CmdExecPath" "$strParamCMD


			$pinfo = New-Object System.Diagnostics.ProcessStartInfo

			$pinfo.FileName		= $CmdExecPath
			$pinfo.Arguments	= $strParamCMD
		
			# The next few lines are required to make sure the process waits for the package execution to finish

			$pinfo.CreateNoWindow			= $true
			$pinfo.UseShellExecute			= $false
			$pinfo.RedirectStandardOutput	= $true
			$pinfo.RedirectStandardError	= $true

			$p = New-Object System.Diagnostics.Process
			$p.StartInfo = $pinfo

			if (!($boolPreProd))
			{
				$null =  $p.Start()			# PDUBOIS le 23/04 pour gagner du temps

				[String] $output = $p.StandardOutput.ReadToEnd()
				[String] $Error  = $p.StandardError.ReadToEnd()
			
				$p.WaitForExit()

				$ExecExitCode = $p.ExitCode			
			}
			else
			{
				Sleep(5)
				$ExecExitCode = 0	
				
			} 
			
			
			Write-Host $output							
			Write-Host "--------------------------------" 	
			Write-Host "Flux ERREUR "
			Write-Host " "		
			Write-Host $Error
			Write-Host "--------------------------------"

			switch ($ExecExitCode)
			{
				
				0 { 
				Write-Host "lastExitCode "$CmdExecPath" value is 0"
				break
				}
							
				default { 
				Write-Host "lastExitCode "$CmdExecPath" value is "$ExecExitCode" ERROR"
				break
				}
				
			}
		}
		catch 
		{		
			$ExecExitCode		= -2
            $boolTraitementEnErreur = $true
			Write-Host "CATCH sur traitement "$strSource
			[string ]$sException = $_.Exception|format-list -force| out-string
			Write-Host  $sException -ForegroundColor Red	
		}
		
		Write-Host "Le traitement "$strSource" se termine avec boolTraitementEnErreur : "$boolTraitementEnErreur
	}
	end 
	{
		$ExecExitCode
	}
}

#===================================================================
# Corps
#===================================================================

Try
{
	
	Export-ModuleMember -variable * –Function *
}
catch
{
	Write-Host "$($_.GetType().FullName)" -ForegroundColor blue
	Write-Host "$($_.Exception.Message)" -ForegroundColor Red
	Write-Host "CATCH erreur dans $($MyInvocation.MyCommand.Definition)"

	exit -2
}
	