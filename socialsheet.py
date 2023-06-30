import xlrd
import xlwt

def main():
    # Open the Excel file for reading
    workbook = xlrd.open_workbook('social.xls')
    worksheet = workbook.sheet_by_index(0)
    # Create a new Excel file for writing
    new_workbook = xlwt.Workbook()
    new_worksheet = new_workbook.add_sheet('Sheet1')
    # Keep track of the last value in column B for each value
    last_values = {}
    # Loop through each row in the worksheet
    for row in range(worksheet.nrows):
        # Get the value in column B for this row
        value = worksheet.cell_value(row, 1)
        
        # Update the last row for this value
        last_values[value] = row
    # Loop through each row in the worksheet again
    new_row = 0
    for row in range(worksheet.nrows):
        # Get the value in column B for this row
        value = worksheet.cell_value(row, 1)
        # If this is the last row for this value, write it to the new worksheet
        if row == last_values[value]:
            for col in range(worksheet.ncols):
                new_worksheet.write(new_row, col, worksheet.cell_value(row, col))
            new_row += 1
    # Save the new Excel file
    new_workbook.save('grad.xls')



if __name__ == '__main__':
    main()
