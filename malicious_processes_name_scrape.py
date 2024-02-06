from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(options=Options())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def process_grabber():
    driver.get('https://www.pcmatic.com/company/libraries/process/top.asp?mode=1') #Gets the website that has the malicious processs names

    tbody = driver.find_element(By.XPATH, '//*[@id="tblProcessTop"]/thead/tr/th[2]') #finds the table that has the names

    processes = [] #list to add the names into

    def scrape(): #function that finds the names and adds them into the list
        for tr in tbody.find_elements(By.XPATH, '//tr'): #loops through the table
            row = [item.text for item in tr.find_elements(By.XPATH, '//td')] #gather the process names into a list
        processes.append(row[1:2])
        processes.append(row[7:8])
        processes.append(row[13:14])
        processes.append(row[19:20])
        processes.append(row[25:26])
        processes.append(row[31:32])
        processes.append(row[37:38])
        processes.append(row[43:44])
        processes.append(row[49:50])
        processes.append(row[55:56])
        
        # processes.append(row) #adds them to the list
            

    scrape() #runs the function

    count = 1 #this will determine how many times the functions runs to scrape all of the process names
    try:
        while (count < 10):
            driver.find_element(By.XPATH, '//*[@id="tblProcessTop_next"]').click() #clicks next to go to the next page to scrape from
            scrape()
            count += 1 # Increases the count
    except Exception:
        print("An Error occurred!!")

    with open('process_names.txt', 'w') as nam:
        for names in processes:
            nam.write(str(names) + '\n')


    # #This removes the square brackets and apostrophes from the malicious processes' names
    # with open('process_names.txt', 'r') as clean:
    #     for line in clean:
    #         processes.append(line[2:-3])

        
    
process_grabber()
