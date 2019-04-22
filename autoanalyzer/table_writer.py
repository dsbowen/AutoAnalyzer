import xlsxwriter

class TableWriter():
    def __init__(self, sum_vars=None, sum_stats=None):
        self.set_sum_stats(sum_vars, sum_stats)
        self.row = self.col = 0
        
    def set_sum_stats(self, sum_vars, sum_stats):
        self.sum_vars = sum_vars
        self.sum_stats = sum_stats
        
    def write(self):
        self._wb = xlsxwriter.Workbook('_Results.xlxs')
        self._add_formats()
        self._ws = self._wb.add_worksheet('Summary stats')
        self._ws.set_column(0, 5, width=20)
        start_row = self.row
        self._write_sum_vars()
        self.row += 1
        [self._write_vgroups(vgroup, self.sum_stats[vgroup]) 
            for vgroup in self.sum_stats]
        self._wb.close()
        
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
        
    def _write_sum_vars(self):
        [self._ws.write(self.row, i+1, sum_var, self._format['center_bold'])
            for i, sum_var in enumerate(self.sum_vars)]
        
    def _write_vgroups(self, vgroup, vgroup_dict):
        self._ws.write(self.row, 0, vgroup, self._format['bold'])
        self.row += 1
        [self._write_subgroups(sg, vgroup_dict[sg])
            for sg in sorted(list(vgroup_dict))]
        self.row += 1
        
    def _write_subgroups(self, sg, sg_dict):
        self._ws.write(self.row, 0, str(sg), self._format['default'])
        [self._write_sum_cell(sum_var, sg_dict[sum_var]) 
            for sum_var in sg_dict]
        self.row += 1
        
    def _write_sum_cell(self, sum_var, sum_var_dict):
        col = self.sum_vars.index(sum_var)+1
        
        cell = '{:.2f} \n ({:.2f}) \n'.format(
            sum_var_dict['mean'], sum_var_dict['std'])
            
        try:
            for pctile, val in sum_var_dict['pctiles']:
                cell += 'p={}: {:.2f} \n'.format(pctile, val)
        except:
            for val, count, in sum_var_dict['val_counts']:
                cell += '{}: {:.2f} \n'.format(val, count)
                
        cell += 'N={}'.format(sum_var_dict['N'])

        self._ws.write(self.row, col, cell, self._format['center'])