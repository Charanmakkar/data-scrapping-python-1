from excel import *
from time import sleep
from selenium import webdriver
from table2excel import *


print("**ALL IMPORTS DONE")

# Start Chrome Driver
chromedriver = 'Users/dell/Documents/MyPrograme/chromedriver'

##driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()

######################main loop#############################
print("**STARTING MAIN LOOP")
for x in range(3):  #maxNumberOfEntries
    hyperLink = readCell(fileToReadEnteriesFrom, ("E"+str(x+1)))
    print(hyperLink)

    # Open the URL you want to execute JS
    URL = 'https://bteup.ac.in/webapp/institutesearch.aspx'
    driver.get(URL)
    driver.execute_script(hyperLink)
    webpage = driver.page_source

    f = open("file.html", "w")
    f.write(webpage)
    f.close()

    r1 = fileTOexcel_Table1()
    r2 = fileTOexcel_Table2()

    insertListToROW(r1, r2)