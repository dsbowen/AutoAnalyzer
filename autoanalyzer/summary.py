##############################################################################
# Summary Block
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

from autoanalyzer.private.block_base import BlockBase
from autoanalyzer.private.writer_base import POOLED_VAL
import xlsxwriter

class Summary(BlockBase):
    def __init__(self, table=None, vars=[], title='Summary Statistics'):
        self._init_block(table, title)
        self.vars(vars)
        
    # Set the summary variables
    def vars(self, vars=[]):
        self._vars = vars
        self._ncols = len(vars)
    
    
    
    ###########################################################################
    # Generate summary statistics
    ###########################################################################
    
    # Generate summary statistics cells
    # must be assigned to a table
    # cells: {vgroup: {vgroup_val: {var: SummaryCell}}}
    def generate(self):
        self._init_cells('summary')
        self._N()
        self._mean()
        self._std()
        self._pctiles()
        self._freq()
        
    def _N(self):
        vars = self._vars
        counts = self._table._vgroup_df.count()
        [self._row_cells[v].N(counts[v]) for v in vars]
            
    def _mean(self):
        vars = [v for v in self._vars
            if self._table._vars[v]['type'] != 'category']
        means = self._table._vgroup_df.mean()
        [self._row_cells[v].mean(means[v]) for v in vars]
            
    def _std(self):
        vars = [v for v in self._vars
            if self._table._vars[v]['type'] in ['binary','ordered','numeric']]
        stds = self._table._vgroup_df[vars].std()
        [self._row_cells[v].std(stds[v]) for v in vars]
        
    def _pctiles(self):
        vars = [v for v in self._vars
            if self._table._vars[v]['type'] == 'numeric']
        for v in vars:
            pctiles = self._table._vars[v]['cell_pctile']
            vals = self._table._vgroup_df[v].quantile(pctiles)
            self._row_cells[v].pctiles(
                [(pctile, val) for pctile, val in zip(pctiles, vals)])
    
    def _freq(self):
        vars = [v for v in self._vars
            if self._table._vars[v]['type'] in ['category','binary','ordered']]
        for v in vars:
            val_counts = self._table._vgroup_df[v].value_counts()
            val_counts = val_counts / self._row_cells[v]._N
            self._row_cells[v].freq(list(zip(val_counts.index, val_counts)))
            
    def _write(self, row, col, ws, format, vgroup_index):
        self._write_block(row, col, ws, format, vgroup_index, 'summary')