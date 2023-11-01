from excel import *
from selenium import webdriver


print("**ALL IMPORTS DONE")

# Start Chrome Driver
chromedriver = 'Users/dell/Documents/MyPrograme/chromedriver'

##driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()

######################main loop#############################
print("**STARTING MAIN LOOP")
for x in range(2):  #maxNumberOfEntries
    hyperLink = readCell(("E"+str(x+1)))
    print(hyperLink)

    # Open the URL you want to execute JS
    URL = 'https://bteup.ac.in/webapp/institutesearch.aspx'
    driver.get(URL)
    driver.execute_script("javascript:__doPostBack('ctl00$ContentPlaceHolder1$GridView1','Select$0')")
    webpage = driver.page_source

    # f = open("file.html", "a")
    # f.write(webpage)
    # f.close()

##import urllib.request as urllib
##from bs4 import BeautifulSoup
##
##URL = "file:///C:/Users/dell/Desktop/Tarun/Website%20wala%20Project/file.html"
##response = urllib.urlopen(URL)
##html_doc = response.read()
##
##soup = BeautifulSoup(html_doc, 'html.parser')
####print (soup.tr.find_all_next)
##masterDiv = soup.find('div',  class_="panel-grid-cell")
####print(soup.find('div',  class_="panel-grid-cell"))
##masterTable1 = soup.find('table', id="ctl00_ContentPlaceHolder1_grd1")
##masterTable2 = soup.find('table', id="ctl00_ContentPlaceHolder1_grdbranch")
