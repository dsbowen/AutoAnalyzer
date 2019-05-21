##############################################################################
# Block Base
# by Dillon Bowen
# last modified 05/21/2019
##############################################################################

from autoanalyzer.data_frame import DataFrame
from autoanalyzer.cells.summary_cell import SummaryCell
from autoanalyzer.cells.analysis_cell import AnalysisCell
from autoanalyzer.bases.writer_base import WriterBase, POOLED_VAL
from autoanalyzer.bases.base import Base

class BlockBase(WriterBase, Base):
    # Initialize block
    def _init_block(self, table, title):
        self.table(table)
        self.title(title)
        self._cells = {}

    # Set the Table or TableGenerator to which this summary block belongs
    def table(self, table=None):
        self._parent(
            new_parent=table, parent_attr='_table', child_attr='_blocks')
        if table is not None:
            self._df = table._df
        else:
            self._df = DataFrame()
        
    # Initialize row of cells
    # type: type of block
    # cells: {vgroup: {vgroup_val: {var: SummaryCell}}}
    # row: row of cells belonging to a particular vgroup value
    def _init_row(self, type):
        vgroup = self._table._vgroup
        val = self._table._vgroup_val
        
        if vgroup not in self._cells:
            self._cells[vgroup] = {}
            
        if type == 'summary':
            self._cells[vgroup][val] = {v: SummaryCell() for v in self._vars}
        elif type == 'analysis':
            self._cells[vgroup][val] = {v: AnalysisCell() 
                for v in self._regressors}
                
        self._row = self._cells[vgroup][val]
        
        
        
    ##########################################################################
    # Write
    ##########################################################################
    
    # Write
    # collect arguments and set column variables
    # write title
    # write heading
    # write data (cells)
    def _write_block(self, row, col, type):
        self._collect_write_args(row, col)
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
            
    # Collect arguments for writing the block
    def _collect_write_args(self, row, col):
        self._row_num = row
        self._col_num = col
        self._ws = self._table._ws
        self._format = self._table._format
        self._vgroup_index = self._table._vgroup_index
        
    # Write the block title
    def _write_block_title(self):
        row = self._row_num
        start_col = self._col_num
        end_col = start_col + self._ncols-1
        self._write_title(
            row, start_col, row, end_col, 
            self._title, self._format['center_bold'])
        [self._ws.write(
            row+1, start_col+i, 
            self._df._vars[v]['label'], self._format['center_bold'])
            for i,v in enumerate(self._cols)]
        
    # Write a single cell
    # arguments:
    #   vgroup: verticle group variables
    #   val: value of the vertical group variable for this cell
    #   col_var: column variable for this cell
    def _write_cell(self, vgroup, val, col_var):
        row = self._vgroup_index[vgroup][val]
        col = self._col_num + self._cols.index(col_var)
        self._cells[vgroup][val][col_var]._write(
            self._ws, row, col, self._format['center'])
      