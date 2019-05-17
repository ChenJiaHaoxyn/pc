
def get_csv(file):
    open(file)
    a=file.read()
    b=file.readline()
    return a,b
import csv
csv_file=csv.reader(open("Stu_csv.csv"))
for stu in csv_file:
    print(stu)
stu1 = ['marry',26]
stu2 = ['bob',23]
out = open('Stu_csv.csv','a', newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print ("write over")


def read_excel():
    import xlrd
    import xlwt
    from datetime import date, datetime
    # 打开文件
    workbook = xlrd.open_workbook(r'F:\demo.xlsx')
    # 获取所有sheet
    print
    workbook.sheet_names()  # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[1]
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('sheet2')
    # sheet的名称，行数，列数
    print
    sheet2.name, sheet2.nrows, sheet2.ncols
    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print
    rows
    print
    cols
    # 获取单元格内容
    print
    sheet2.cell(1, 0).value.encode('utf-8')
    print
    sheet2.cell_value(1, 0).encode('utf-8')
    print
    sheet2.row(1)[0].value.encode('utf-8')
    # 获取单元格内容的数据类型
    print
    sheet2.cell(1, 0).ctype
if __name__ == '__main__':
    read_excel()

import os
os.getcwd()
os.listdir(os.getcwd())
os.path.split('D:\\pythontest\\ostest\\Hello.py')
os.path.split('.')
os.path.split('D:\\pythontest\\ostest\\')
os.path.split('D:\\pythontest\\ostest')
os.path.join('D:\\pythontest', 'ostest')
os.path.join('D:\\pythontest\\ostest', 'hello.py')
os.path.join('D:\\pythontest\\b', 'D:\\pythontest\\a')

import datetime
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
print ((endtime - starttime).seconds)