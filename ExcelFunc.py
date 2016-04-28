# -*- encoding:utf-8 -*-
import xlrd


class ReadTestData:
    '''
    读取excel测试数据
    '''
    def __init__(self, path, sheet_name):
        path = unicode(path, 'utf-8')
        sheet_name = unicode(sheet_name, 'utf-8')
        self.open_book = xlrd.open_workbook(path)

        self.sheetName = self.open_book.sheet_by_name(sheet_name)
    # def get_sheet(self, sheet_name):
    #     '''
    #     获取要操作的sheet对象
    #     :param sheet_name:
    #     :return:
    #     '''
    #     self.sheetName = self.open_book.sheet_by_name(sheet_name)
    #     return self.sheetName

    def get_nrow(self):
        '''
        获取行数
        :return:
        '''
        return self.sheetName.nrows
    def get_ncol(self):
        '''
        获取列数
        :return:
        '''
        return self.sheetName.ncols

    def get_row_value(self, test_name):
        '''
        根据测试名称获取该行所有的数据
        :param test_name:测试名称
        :return:
        '''
        cols = self.sheetName.col_values(0)
        for i in range(len(cols)):
            if cols[i].encode('utf-8') == test_name:
                return self.sheetName.row_values(i)