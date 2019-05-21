##############################################################################
# Table
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

from autoanalyzer.bases.table_base import TableBase
from autoanalyzer.bases.writer_base import WriterBase, POOLED_VAL
from copy import deepcopy

'''
Data:
    title
    vars: {var: {'label', 'type', 'group_pctile', 'cell_pctile'}}
    tgroup_title: subtitle from table group variable
    df: pandas DataFrame
    vgroups: {vgroup: [group values]}
    blocks: summary and analysis blocks
    ncols: number of columns
'''
class Table(TableBase, WriterBase):
    def __init__(self, table_generator):
        self._title = table_generator._title
        self._ws_title = table_generator._ws_title
        self._vars = deepcopy(table_generator._vars)
        self.tgroup_title(table_generator._tgroup, table_generator._tgroup_val)
        self._df = table_generator._tgroup_df
        self._vgroups = deepcopy(table_generator._vgroups)
        self._blocks = []
        [b.table(self) for b in deepcopy(table_generator._blocks)]
        self._ncols = sum([b._ncols for b in table_generator._blocks])
        
    # Set table group title (subtitle)
    def tgroup_title(self, tgroup, tgroup_val):
        if tgroup == 'Pooled':
            self._tgroup_title = 'Pooled'
            return
        self._tgroup_title = self._vars[tgroup]['label']+' = '+str(tgroup_val)



    ##########################################################################
    # Generate table statistics
    ##########################################################################
    
    # Generate table statistics
    def generate(self):
        [self._generate_by_vgroup(v) for v in self._vgroups]
        self._vgroup = 'Pooled'
        self._generate_by_vgroup_val(pooled=True)
        return self
        
    # Generate table statistics by vertical group variable
    def _generate_by_vgroup(self, vgroup):
        self._vgroup = vgroup
        series, values = self._get_series_values(vgroup)
        values = sorted(list(values))
        self._vgroups[vgroup] = values
        [self._generate_by_vgroup_val(series, v) for v in values]
        
    # Generate statistics for a single value of the vertical group variable
    # analysis may be pooled over vertical group variable
    def _generate_by_vgroup_val(self, series=None, val=None, pooled=False):
        if pooled:
            self._vgroup_df = self._df
            self._vgroup_val = POOLED_VAL
        else:
            self._vgroup_df = self._df[series==val]
            self._vgroup_val = val
        [block.generate() for block in self._blocks]
    
    
    
    ##########################################################################
    # Write table
    ##########################################################################
    
    def _write(self, ws, row, format):
        self._ws, self._row, self._format = ws, row, format
        self._write_table_title()
        self._write_table_title(self._tgroup_title)
        block_row_start = self._row
        self._row += 2
        self._write_vgroups()
        col = 1
        for b in self._blocks:
            b._write(
                block_row_start, col, 
                self._ws, self._format, self._vgroup_index)
            col += b._ncols
        return self._row
        
    def _write_table_title(self, title=None):
        if title is None:
            title = self._title
        self._write_title(
            self._row, 1, self._row, self._ncols, 
            title, self._format['center_bold'])
        self._row += 1
        
    def _write_vgroups(self):
        vgroups = list(self._vgroups)+['Pooled']
        self._vgroup_index = {vgroup: {} for vgroup in vgroups}
        [self._write_vgroup(v) for v in vgroups]
        self._row += 1
        
    def _write_vgroup(self, vgroup):
        if vgroup == 'Pooled':
            label, vals = 'Pooled', [POOLED_VAL]
        else:
            label, vals = self._vars[vgroup]['label'], self._vgroups[vgroup]
        self._ws.write(self._row, 0, label, self._format['bold'])
        for val in vals:
            self._row += 1
            self._ws.write(self._row, 0, str(val), self._format['default'])
            self._vgroup_index[vgroup][val] = self._row
        self._row += 2