import xlrd
from xlutils.copy import copy

FILE_PATH = "SOE_Data.xls"
NEW_FILE_PATH = "SOE_Data_Formatted.xls"

def parse():
    reference = {}
    new_values = []
    workbook = xlrd.open_workbook(FILE_PATH)
    sheet = workbook.sheet_by_index(0)
    for row in range(2, 252):
        key = sheet.cell_value(row, 1).strip()
        value = sheet.cell_value(row, 1)
        reference[key] = value
    for row in range(6, 253):
        key = sheet.cell_value(row, 1).strip()
        value = reference.get(key, 0)
        new_values.append(value)
    wb = send(workbook)
    sheet = wb.get_sheet(0)
    for row, value in (new_values, 2):
        sheet.write(row, 5, value)
    wb.save(NEW_FILE_PATH)


if __name__ == '__main__':
    parse()