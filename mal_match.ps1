#This script matches the malicious process names from the mal_names.txt file to the proceses on the machine to see if they match

$Mnames = Get-Content "mal_names.txt" #This accesses the mal_name.txt file and retrieves all its contents
$Processes = Get-Process | Select-Object Path | Split-Path -leaf -ErrorAction SilentlyContinue #This retrieves the processes along with their extension only 

foreach($Name in $Mnames){ #This function loops through both the malicious names and the processes running on the machine and compare them
    foreach($process in $Processes){
        
        if($Process -eq $Name){
            Write-Output "****MATCHING MALICIOUS PROCESS NAME DETECTED!!!!!!****" 
            Write-Output "System process name: " $Process " VS " "Malicious process name: " $Name
            Write-Output "   " #Puts a space between the results
        }
        
    }
        
}
