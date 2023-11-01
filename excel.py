from openpyxl import Workbook, load_workbook

def EXCEL1():
    excel_file = "book1.xlsx"
    workbook = load_workbook(excel_file)
    worksheet = workbook.active

    maxNumberOfRows = worksheet.max_row
    maxNumberOfColumns = worksheet.max_column


def readCell(cellvalue):
    value = worksheet[cellvalue].value
##    print(value)
    return value
def readMaxCol(fileName):
    excel_file = fileName
    workbook = load_workbook(excel_file)
    worksheet = workbook.active
    maxNumberOfColumns = worksheet.max_column

def readMaxRow(fileName):
    excel_file = fileName
    workbook = load_workbook(excel_file)
    worksheet = workbook.active
    maxNumberOfColumns = worksheet.max_row
    



##readCell("A1")







### Write data to the worksheet
##for x in range(1, worksheet.max_row+1):
##    hyper = worksheet.cell(row = x, column = 4). hyperlink.display
##    cell = "F"+str(x)
##    worksheet[cell] = hyper
##
### Save the workbook to the Excel file
##workbook.save(excel_file)
