
import openpyxl
#import xlsxwriter
from openpyxl.cell.cell import Cell
from backend.Processing.Report import Report

class reportExcelExporter:
    MAX_COL = 50
    MAX_ROW = 100
    def __init__(self,path:str,) -> None:
        self.file_type = '.xlsx'
        self.path = path
        self.workbook = openpyxl.load_workbook(filename = self.path)

        self.sheet_name = self.workbook.sheetnames[0]
        self.sheet = self.workbook[self.sheet_name]

        self.__find_codes()

    def save(self,path):
        if path[-len(self.file_type):] != self.file_type:
            path = path + self.file_type
        self.workbook.save(path)
    
    def __find_codes(self,):
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
            cell2.font = cell2.font
            cell2.border = cell2.border
            cell2.fill = cell2.fill
            cell2.number_format = cell2.number_format
            cell2.protection = cell2.protection
            cell2.alignment = cell2.alignment

    def export(self, report:Report):
        for code,pos in self.codes.items():
            
            if code == '%NAME%':
                self.sheet.cell(*pos).value = report.name

            if code == '%DATE%':
                self.sheet.cell(*pos).value = report.date.strftime('%Y-%M-%D')
            

# if __name__ == '__main__':
#     excel = reportExcelExporter('format.xlsx',None)
#     excel.find_codes()
#     excel.save('testtt')
    
#     pass