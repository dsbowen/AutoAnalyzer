##############################################################################
# Table Writer
# by Dillon Bowen
# last modified 05/21/2019
##############################################################################

from autoanalyzer.table_generator import TableGenerator
import xlsxwriter

'''
Data:
    file_name
    worksheets: {ws title: [Worksheet, current row]}
    tables: [Table or TableGenerator]
    generated_tables: [Table] after generate()
'''
class Writer():
    def __init__(self, file_name=None):
        self.file_name(file_name)
        self._worksheets = {}
        self._tables = []
        self._generated_tables = []
        
    # Set file name
    def file_name(self, file_name=None):
        if file_name is None:
            file_name = '_Results'
        self._file_name = file_name
        
    # Write tables
    def write(self):
        self._generate_tables()
        self._init_workbook()
        [self._write_table(table) for table in self._generated_tables]
        self._wb.close()
        
    # Generate tables
    # note that 'table' may be Table or TableGenerator
    def _generate_tables(self):
        self._generated_tables = []
        for table in self._tables:
            if type(table) == TableGenerator:
                self._generated_tables.extend(table.generate())
            else:
                self._generated_tables.append(table.generate())
        
    # Initialize a new workbook
    # initialize workbook
    # add formats
    def _init_workbook(self):
        self._wb = xlsxwriter.Workbook(self._file_name+'.xlsx')

        self._format = {}
        self._format['default'] = self._wb.add_format()
        self._format['bold'] = self._wb.add_format({'bold': True})
        self._format['center'] = self._wb.add_format({'center_across': True})
        self._format['center_bold'] = self._wb.add_format(
            {'center_across': True, 'bold': True})
        for format in self._format.values():
            format.set_text_wrap(True)
            format.set_align('vcenter')
           
    # Write a single table to the workbook
    # if table belongs to new worksheet, initialize worksheet
    # write table to worksheet
    def _write_table(self, table):
        ws_title = table._ws_title
        if ws_title not in self._worksheets:
            ws = self._wb.add_worksheet(ws_title)
            ws.set_column(0, 99, width=20)
            self._worksheets[ws_title] = [ws, 0]
            
        self._worksheets[ws_title][1] = table._write(
            *self._worksheets[ws_title]) - 1