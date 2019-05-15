##############################################################################
# Block Base
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

from autoanalyzer.private.summary_cell import SummaryCell
from autoanalyzer.private.analysis_cell import AnalysisCell
from autoanalyzer.private.writer_base import WriterBase, POOLED_VAL

class BlockBase(WriterBase):
    # Initialize block
    def _init_block(self, table, title):
        self.table(table)
        self.title(title)
        self._cells = {}

    # Set the Table or TableGenerator to which this summary block belongs
    def table(self, table=None):
        try:
            self._table.remove(self)
        except:
            pass
        if table is not None:
            table._blocks.append(self)
        self._table = table
        
    # Set block title
    def title(self, title='Summary Statistics'):
        self._title = title
        
    # Initialize cells dictionary
    def _init_cells(self, type):
        self._vgroup  = self._table._vgroup
        self._vgroup_val = self._table._vgroup_val
        if self._vgroup not in self._cells:
            self._cells[self._vgroup] = {}
        if type == 'summary':
            self._cells[self._vgroup][self._vgroup_val] = {v: SummaryCell()
                for v in self._vars}
        elif type == 'analysis':
            self._cells[self._vgroup][self._vgroup_val] = {v: AnalysisCell()
                for v in self._regressors}
        self._row_cells = self._cells[self._vgroup][self._vgroup_val]
        
        
        
    ###########################################################################
    # Write to table
    ###########################################################################
    
    # Write
    # write title
    # write heading
    # write data (cells)
    def _write_block(self, row, col, ws, format, vgroup_index, type):
        self._row, self._col, self._ws, self._format, self._vgroup_index = (
            row, col, ws, format, vgroup_index)
        if type == 'summary':
            self._cols = self._vars
        elif type == 'analysis':
            self._cols = self._regressors
        self._write_block_title()
        vgroups = self._table._vgroups
        vgroups['Pooled'] = [POOLED_VAL]
        
        [self._write_cell(vgroup, val, var) 
            for vgroup in vgroups for val in vgroups[vgroup]
            for var in self._cols]
        
    def _write_block_title(self):
        self._write_title(
            self._row, self._col, self._row, self._col+self._ncols-1, 
            self._title, self._format['center_bold'])
        [self._ws.write(
            self._row+1, self._col+i, 
            self._table._vars[v]['label'], self._format['center_bold'])
            for i,v in enumerate(self._cols)]
        
    def _write_cell(self, vgroup, val, var):
        row = self._vgroup_index[vgroup][val]
        col = self._col + self._cols.index(var)
        self._cells[vgroup][val][var]._write(
            self._ws, row, col, self._format['center'])
      