import xlrd


def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)                      # 打开工作簿
    sheets = workbook.sheet_names()                          # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])            # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()


if __name__ == "__main__":
    read_excel_xls(r"I:\Py_Project\data")
