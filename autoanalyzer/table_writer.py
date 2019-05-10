##############################################################################
# Table Writer
# by Dillon Bowen
# last modified 05/09/2019
##############################################################################

from autoanalyzer.table import Table
import xlsxwriter

class TableWriter():
    def __init__(self, file_name=None, tables=[]):
        self.file_name(file_name)
        self.tables(tables)
        self._row = self._col = 0
        
    # Set file name
    def file_name(self, file_name=None):
        if file_name is None:
            file_name = '_Results'
        self._file_name = file_name
        
    # Set tables
    # tables: [Table]
    def tables(self, tables=[]):
        if type(tables) == Table:
            tables = [tables]
        self._tables = tables
        
    # Write tables
    def write(self):
        self._init_table()
        [self._write_table(table) for table in self._tables]
        self._wb.close()
        
    # Initialize a new table to write
    def _init_table(self):
        self._wb = xlsxwriter.Workbook(self._file_name+'.xlsx')
        self._add_formats()
        self._ws = self._wb.add_worksheet('Summary stats')
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
        self._table = table
        start_row = self._row
        self._write_sum_vars_header()
        self._row += 1
        [self._write_vgroups(vgroup, table._sum_stats[vgroup]) 
            for vgroup in table._sum_stats]
        
    # Write the header for summary variables
    def _write_sum_vars_header(self):
        [self._ws.write(self._row, i+1, sum_var, self._format['center_bold'])
            for i, sum_var in enumerate(self._table._sum_vars)]
        
    # Write the section of the table associated with a vertical group variable
    def _write_vgroups(self, vgroup, vgroup_dict):
        self._ws.write(self._row, 0, vgroup, self._format['bold'])
        self._row += 1
        [self._write_subgroups(sg, vgroup_dict[sg])
            for sg in sorted(list(vgroup_dict))]
        self._row += 1
        
    # Write the section of the table associated with a vertical subgroup
    def _write_subgroups(self, sg, sg_dict):
        self._ws.write(self._row, 0, str(sg), self._format['default'])
        [self._write_sum_cell(sum_var, sg_dict[sum_var]) 
            for sum_var in sg_dict]
        self._row += 1
        
    # Write a single summary statistic cell
    def _write_sum_cell(self, sum_var, sum_var_dict):
        col = self._table._sum_vars.index(sum_var)+1
        
        cell = '{:.2f} \n ({:.2f}) \n'.format(
            sum_var_dict['mean'], sum_var_dict['std'])
            
        try:
            for pctile, val in sum_var_dict['pctiles']:
                cell += 'p{} = {:.2f} \n'.format(pctile, val)
        except:
            for val, count, in sum_var_dict['val_counts']:
                cell += '{}: {:.2f} \n'.format(val, count)
                
        cell += 'N={}'.format(sum_var_dict['N'])

        self._ws.write(self._row, col, cell, self._format['center'])