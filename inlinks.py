import xlrd
import xlwt
from xlwt import Workbook

FILE_PATH = 'outlinks.xls'
NEW_PATH = 'outlinksformatted.xls'


def parse():
    counter = 0 
    dictionary = {}
    workbook = xlrd.open_workbook(FILE_PATH)
    sheet = workbook.sheet_by_index(0)
    keylist =[]
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    file = open('inlinks.txt', 'w')
    checker = 0
    lists = []
    i = 1

    for row in range(1, 5017):
        key = sheet.cell_value(row, 1).strip()
        keylist.append(key)
    keylist.sort()
    myset = set(keylist)
    for i in myset:
        lists.append(i)
    lists.sort()
    print(len(lists))
    for keys in keylist:
        if(lists[checker] == keys):
            counter+=1
        else:
            dictionary[lists[checker]] = counter
            string = lists[checker] + '            ' + str(counter) + '\n\n'
            file.writelines(string)
            checker+=1
            counter = 0
    dictionary[lists[len(lists)-1]] = keylist.count(lists[len(lists)-1])
    for i in range(len(lists)):
        sheet1.write(i, 0, lists[i])
        sheet1.write(i, 1, dictionary[lists[i]])
    checker = 0
    wb.save(NEW_PATH)

if __name__ == '__main__':
    parse()