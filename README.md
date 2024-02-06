# malicious-process-name-search-
Here's a list of the items in this repository and their functions;

1). maliciopus_processes_name_scrape.py - This Python program opens a browser with the specified url for the site that has the names of malicious processes listed. It then collects every process name from the table and skips to the next page, collects every process name again. It does this until it has been through all 10 pages. These are then added into a list that will later be added to a txt file. 

2). clean_txt.py - Cleaning the list from the malcious_processes_name_scrape.py program was giving me a little challenge, so I just built this quick fix to it that removes the brackets and apostrophes and presents only the malicious process names. run "python3 clean_txt.py > <choose new name.txt" to pipe the results into a new txt file if you'd like.

3). mal_match.ps1 -  This is the PowerShell script that'll match the malicious processes from the txt file and the processes that are running on your computer to see if any of them match. There is a high chance that you'll see some Windows processes popup as matches, hash those executables and use that hash to investigate, also check their signatures to see if they are legit! 
