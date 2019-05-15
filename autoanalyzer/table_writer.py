##############################################################################
# Table Writer
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

from autoanalyzer.table_generator import TableGenerator
from autoanalyzer.table import Table
from autoanalyzer.private.writer_base import WriterBase, POOLED_VAL
import xlsxwriter

class TableWriter(WriterBase):
    def __init__(self, file_name=None):
        self.file_name(file_name)
        self._tables = []
        self._generated_tables = []
        self._row = self._col = 0
        
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
    def _generate_tables(self):
        self._generated_tables = []
        for table in self._tables:
            if type(table) == TableGenerator:
                self._generated_tables.extend(table.generate())
            else:
                self._generated_tables.append(table.generate())
        
    # Initialize a new workbook to write
    def _init_workbook(self):
        self._wb = xlsxwriter.Workbook(self._file_name+'.xlsx')
        self._add_formats()
        self._ws = self._wb.add_worksheet('Sheet1')
        self._ws.set_column(0, 99, width=20)
        
    # Add formats to the workbook
    def _add_formats(self):
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
    def _write_table(self, table):
        self._row = table._write(self._ws, self._row, self._format) - 1