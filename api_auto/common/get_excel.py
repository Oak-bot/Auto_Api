import xlrd #导入Excel操作包

class Get_Excel:
    def __init__(self):
        self.excel = xlrd.open_workbook('../testdata/api_auto.xlsx')  # 打开文件,文件地址要用相对路径不要用绝对路径，以免在其他机器执行时找不到
        self.testsuite = self.excel.sheet_by_name('testsuite')
        self.names = self.excel.sheet_names()#获取所有的sheet名

    def get_testsuite(self):
        '''
        获取用例集是否可以执行
        :return:返回可执行的sheet页
        :rtype:字典
        '''
        title = []#获取各用例集
        for i in range(1, self.testsuite.nrows):
            title.append(self.testsuite.cell_value(i,0))
        data1 = []#获取各用例是否执行
        for i in range(1, self.testsuite.nrows):
            data1.append(self.testsuite.cell_value(i,1))
        data = []#拼装testsuite为字典
        data.append(dict(zip(title,data1)))
        return data[0]

    def get_case(self):
        '''
        :return: 返回本文件中所有可执行的用例
        :rtype:列表
        '''
        get_suite = self.get_testsuite()#初始化用例集管理
        data1 = []
        for i in self.names[1:]:#从第二个sheet遍历所有sheet页
            if get_suite[f'{i}'] == 'do':
                table = self.excel.sheet_by_name(f'{i}')#找出所有可以执行的用例集
                for i in range(1,table.nrows):
                    if table.cell_value(i, 2) == 'Y':#找出所有可执行用例集中可执行的用例
                        data1.append(table.row_values(i))
        return data1

    def get_nrows(self):#获取总行数
        return self.table.nrows

# i = Get_Excel()
# print(i.get_case())


    # def get_excel_row(self):
    #     '''
    #     获取标记为执行的用例
    #     :return:返回用例列表
    #     :rtype:
    #     '''
    #     data1 = []
    #     # title = self.table.row_values(0)
    #     for i in range(1,self.table.nrows):
    #         # print(table.row_values(i))
    #         # data.append(dict(zip(title,table.row_values(i))))
    #         if self.table.cell_value(i,2) == 'Y':
    #             data1.append(self.table.row_values(i))
    #     return data1
# print(table.nrows)#显示总行数
# print(table.ncols)#显示总列数elf
# print(table.row_values(0))#读取第一行的数据
# print(table.col_values(0))#读取第一列的数据
# print(table.cell_value(0,1))#读取第一行第二列的信息，前面是行，后面是列
# for i in range(1,table.nrows):
#     print((table.cell_value(i,1)),(table.cell_value(i,2)))
# return (table.cell_value(row,2)),(table.cell_value(row,3))
# return (table.row_values(row))
# print(get_excel_row(1))

