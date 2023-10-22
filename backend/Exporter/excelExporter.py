if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())

import openpyxl
from openpyxl.cell.cell import Cell
from openpyxl.chart import  Reference, Series, BarChart
import copy
#from openpyxl.chart.series import Series

from backend.Processing.Report import Report

class excelExporter:
    MAX_ROW = 100
    MAX_COL = 100
    def __init__(self,path_format:str,) -> None:
        self.file_type = '.xlsx'
        self.path_format = path_format
        self.workbook = openpyxl.load_workbook(filename = self.path_format)
        self.sheet_name = self.workbook.sheetnames[0]
        self.sheet = self.workbook[self.sheet_name]

        self.__find_codes__()
    
    def __find_codes__(self,):
        self.codes = {}
        for i in range(1,self.MAX_ROW):
            for j in range(1,self.MAX_COL):
                value = self.sheet.cell(row=i, column=j).value
                if value is not None:
                    value = value.strip()

                    if len(value) > 3:
                        if value[0] == '%' and value[-1] == '%':
                            self.codes[value.upper()] = (i,j)
        

    def copy_style(self,cell1:Cell, cell2:Cell):
        """copy style of cell1 into cell2
        """
        if cell1.has_style:
            cell2.font = cell1.font.copy()
            cell2.border = cell1.border.copy()
            cell2.fill = cell1.fill.copy()
            cell2.number_format = cell1.number_format
            cell2.protection = cell1.protection.copy()
            cell2.alignment = cell1.alignment.copy()

    def save(self,path):
        try:
            if len(path) > len(self.file_type):
                if path[-len(self.file_type):] != self.file_type:
                    path = path + self.file_type
            else:
                path = path + self.file_type

            self.workbook.save(path)
            return True, None
        except Exception as e:
            return False, str(e)
    

    def __set_list_values__(self, datas:list, start_pos:tuple[int], oriation='v') -> int:
        """set list values into excel, this function inster rows or colums from start point

        Args:
            datas (list): list of data
            start_pos (tuple[int]): _description_
            oriation (str, optional): _description_. Defaults to 'v'.

        Returns:
            int: number of row or col insert
        """
        i,j = start_pos
        # count = len(datas)
        # if oriation.lower() == 'h':
        #     self.sheet.insert_cols(i+1, count - 1)
        #     self.__update_pos(start_pos, 0, count -1)

        # elif oriation.lower() == 'v':
        #     self.sheet.insert_rows(j+1, count - 1)
        #     self.__update_pos(start_pos, count -1, 0)


        for data in datas:
            self.copy_style(self.sheet.cell(*start_pos), 
                            self.sheet.cell(i,j))
            self.sheet.cell(i,j).value = data
            if oriation.lower() == 'h':
                j+=1
            elif oriation.lower() == 'v':
                i+=1


class reportExcelExporter(excelExporter):
    MAX_COL = 50
    MAX_ROW = 100
    

    def __update_pos(self, start_pos, insert_col, insert_row):
        for code, pos in self.codes.items():
            pos = list(pos)
            if pos[0] > start_pos[0]:
                pos[0] = pos[0] + insert_row
            
            if pos[1] > start_pos[1]:
                pos[1] = pos[1] + insert_col
            
            pos = tuple(pos)
            self.codes[code] = pos
            


    def render(self, report:Report):
        range_statistics = report.get_ranges_statistics()
        global_statistics = report.get_global_statistics()
        
        wrong_codes = []
        
        for code,pos in self.codes.items():
            datas = None

            if code == '%NAME%':
                self.sheet.cell(*pos).value = report.name

            elif code == '%DATE%':
                self.sheet.cell(*pos).value = report.date.strftime('%Y-%M-%D')
            
            elif code == '%TIME%':
                self.sheet.cell(*pos).value = report.time.strftime('%H:%m')

            elif code == '%USER%':
                self.sheet.cell(*pos).value = report.username
            
            elif code == '%STANDARD%':
                self.sheet.cell(*pos).value = report.standard['name']
            
            elif code == '%TOTAL_AVRAGE%':
                self.sheet.cell(*pos).value = global_statistics['avrage']
            
            elif code == '%TOTAL_STD%':
                self.sheet.cell(*pos).value = global_statistics['std']
            
            elif code in ['%RANGE_NAME_VERTICALLY%', '%RANGE_NAME_HORIZONTAL%']:
                datas = report.ranges_string
            
            elif code in ['%RANGE_PERCENT_VERTICALLY%', '%RANGE_PERCENT_HORIZONTAL%']:
                datas = list(map(lambda x:x['percent'], range_statistics))
            
            elif code in ['%RANGE_AVRAGE_VERTICALLY%', '%RANGE_AVRAGE_HORIZONTAL%']:
                datas = list(map(lambda x:x['avrage'], range_statistics))

            elif code in ['%RANGE_STD_VERTICALLY%', '%RANGE_STD_HORIZONTAL%']:
                datas = list(map(lambda x:x['std'], range_statistics))

            else:
                wrong_codes.append(code)

            if datas is not None:
                if 'VERTICALLY' in code:
                    self.__set_list_values__(datas, pos, oriation='v')

                elif 'HORIZONTAL' in code:
                    self.__set_list_values__(datas, pos, oriation='h')


        # chart:BarChart = self.sheet._charts[0]
        # x = Reference(self.sheet, min_row=10, min_col=1, max_col=5)
        # y = Reference(self.sheet, min_row=11, min_col=1, max_col=5)
        # s = Series(values=y, xvalues=x)
        # chart.add_data(y)
        # chart.set_categories(x)
        #self.sheet.add_chart(copy.deepcopy(chart))
        return wrong_codes       




class compareExcelExporter(excelExporter):
    MAX_COL = 100
    MAX_ROW = 100

            

    def render(self, reports:list[Report]):
        
        wrong_codes = []
        
        for code,pos in self.codes.items():
            datas = None


            if code in ['%NAMES_VERTICALLY%', '%NAMES_HORIZONTAL%']:
                datas = list(map(lambda x:x.name, reports))

            elif code in ['%DATES_VERTICALLY%', '%DATES_HORIZONTAL%']:
                datas = list(map(lambda x:x.date.strftime('%Y-%M-%D'), reports))

            elif code in ['%TIMES_VERTICALLY%', '%TIMES_HORIZONTAL%']:
                datas = list(map(lambda x:x.time.strftime('%H:%m'), reports))
            
            elif code in ['%USERS_VERTICALLY%', '%USERS_HORIZONTAL%']:
                datas = list(map(lambda x:x.time.strftime('%H:%m'), reports))

            elif code in ['%RANGES_NAME_VERTICALLY%', '%RANGES_NAME_HORIZONTAL%']:
                datas = reports[0].standard['ranges']
            


            else:
                wrong_codes.append(code)

            if datas is not None:
                if 'VERTICALLY' in code:
                    self.__set_list_values__(datas, pos, oriation='v')

                elif 'HORIZONTAL' in code:
                    self.__set_list_values__(datas, pos, oriation='h')
            
        return wrong_codes


    


if __name__ == '__main__':
    from backend.Utils.StorageUtils import objectSaver

    report = objectSaver.load(r'C:\Users\amir\AppData\Local\Dorsa-PSA-Reports\20231021_1524_admin_20231021_152422\report')
    excel = reportExcelExporter(r'files\export_formats\report_format.xlsx')
    excel.render(report)
    excel.save('testtt')
    
    pass