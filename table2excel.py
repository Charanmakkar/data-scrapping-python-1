from excel import *
from bs4 import BeautifulSoup
import pandas as pd

file_path = 'file.html'

with open(file_path, 'r', encoding='ISO-8859-1') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

##table = soup.find('table', id="ctl00_ContentPlaceHolder1_grd1")

table_data = []
def fileTOexcel():
    # Extract table data and organize it into a list of lists
    
    table = soup.find('table', id="ctl00_ContentPlaceHolder1_grd1")
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
        table_data.append(row_data)

    institute_details = row_data[0]
##    print(institute_details)
    institute_details = institute_details.split(":")
    instituteCode = institute_details[1].split("INSTITUTE NAME")[0]
    instituteName = institute_details[1].split("INSTITUTE NAME")[1]

    institute_details = row_data[1]
##    print(institute_details)
    institute_details = institute_details.split(":")
    phoneNumber = institute_details[-2].split("ALTERNATIVEMOBILENUMBER")[0]
    alternateNumber = institute_details[-1]
    webSite = institute_details[1].split("EMAILID")[0]
    emailId = institute_details[2].split("MOBILE")[0]

    institute_details = row_data[2]
##    print(institute_details)
    address = institute_details.split(":")[1][:-8]
    district = institute_details.split(":")[-2][:-7]
    pincode = institute_details.split(":")[-1]

    return 1

### Create a DataFrame from the table data
##df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Assuming the first row contains column headers
##
### Write the DataFrame to an Excel file
##df.to_excel('output_data2.xlsx', index=False)
##
##########################################################################
##
##table = soup.find('table', id="ctl00_ContentPlaceHolder1_grdbranch")
##
### Extract table data and organize it into a list of lists
##table_data = []
##for row in table.find_all('tr'):
##    row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
##    table_data.append(row_data)

# Create a DataFrame from the table data
##df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Assuming the first row contains column headers
##
### Write the DataFrame to an Excel file
##df.to_excel('output_data.xlsx', index=False)



"""
table_data[1][1].find("mobile")
-1
table_data[1][1][-10:]
'8328908142'
table_data[1][1][-10:]
'8328908142'
len("ALTERNATIVEMOBILENUMBER:")
24
table_data[1][1][-44:-34]
'9412391802'
"""
result = fileTOexcel()
