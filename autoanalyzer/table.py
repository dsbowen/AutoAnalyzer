##############################################################################
# Table
# by Dillon Bowen
# last modified 05/23/2019
##############################################################################

from autoanalyzer.bases.table_base import TableBase
from autoanalyzer.bases.writer_base import WriterBase, POOLED_VAL
from copy import deepcopy

'''
Data:
    title
    tgroup_title: subtitle from table group variable
    df: DataFrame
    vgroups: {vgroup: [group value]}
    blocks: summary and analysis blocks
    row: row number
    vgroup_index: {vertical group variable value: row}
    writer: parent Writer
'''
class Table(TableBase, WriterBase):
    def __init__(self, table_generator):
        self._df = table_generator._tgroup_df
        self._ws_title = table_generator._ws_title
        self._title = table_generator._title
        self.tgroup_title(
            table_generator._tgroup, table_generator._tgroup_val)
        self._vgroups = deepcopy(table_generator._vgroups)
        self._blocks = []
        to_add = deepcopy(table_generator._blocks)
        while to_add:
            to_add.pop(0).table(self)
        self._writer = table_generator._writer
        
    # Set table group title (subtitle)
    # tgroup: table group variable
    # val: value of the table group variable for this table
    def tgroup_title(self, tgroup, val):
        if tgroup == 'Pooled':
            self._tgroup_title = 'Pooled'
            return
        self._tgroup_title = self._df._vars[tgroup]['label']+' = '+str(val)



    ##########################################################################
    # Generate table statistics
    ##########################################################################
    
    # Generate table statistics
    # generate by vertical group variables and pooled
    def generate(self):
        self._decorate()
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
    # arguments:
    #   series: Series with split values of the vertical group variable
    #   val: selected value of the series
    #   pooled: indicator to pool analysis over vertical groups
    def _generate_by_vgroup_val(self, series=None, val=None, pooled=False):
        if pooled:
            self._vgroup_df = self._df
            self._vgroup_val = POOLED_VAL
        else:
            self._vgroup_df = self._df[series==val]
            self._vgroup_val = val
        [b.generate() for b in self._blocks]
    
    
    
    ##########################################################################
    # Write table
    ##########################################################################
    
    # Write table
    # collect arguments
    # write title and subtitle
    # write column labelling vertical groups and values
    # write blocks
    # return: ending row
    def _write(self, ws, row):
        self._ws, self._row, self._format = ws, row, self._writer._format
        
        self._write_table_title()
        self._write_table_title(self._tgroup_title)
        
        block_row_start = self._row
        self._row += 2
        self._write_vgroups()
        
        col = 1
        for b in self._blocks:
            b._write(block_row_start, col)
            col += b.ncols()
        return self._row
        
    # Write table title or subtitle
    def _write_table_title(self, title=None):
        if title is None:
            title = self._title
        self._write_title(
            self._row, 1, self._row, self.ncols(), 
            title, self._format['center_bold'])
        self._row += 1
        
    # Write column with vertical group variables and values
    # initialize vertical group index dictionary: {vgroup value: row}
    def _write_vgroups(self):
        vgroups = list(self._vgroups)+['Pooled']
        self._vgroup_index = {vgroup: {} for vgroup in vgroups}
        [self._write_vgroup(v) for v in vgroups]
        self._row += 1
        
    # Write a single vertical group variable and values
    # get vertical group lable and values
    # write label and values
    # increment row
    def _write_vgroup(self, vgroup):
        if vgroup == 'Pooled':
            label, vals = 'Pooled', [POOLED_VAL]
        else:
            label = self._df._vars[vgroup]['label']
            vals = self._vgroups[vgroup]
            
        self._ws.write(self._row, 0, label, self._format['bold'])
        for val in vals:
            self._row += 1
            self._ws.write(self._row, 0, str(val), self._format['default'])
            self._vgroup_index[vgroup][val] = self._row
            
        self._row += 2