##############################################################################
# Summary Block
# by Dillon Bowen
# last modified 05/24/2019
##############################################################################

from autoanalyzer.bases.block_base import BlockBase
from autoanalyzer.bases.writer_base import POOLED_VAL
from copy import deepcopy
import xlsxwriter

'''
Data:
    title
    vars: [summary variable]
    cells: {vgroup: {vgroup_val: {var: SummaryCell}}}
    row: [cell] belonging to a particular vgroup value
    table: parent Table
'''
class Summary(BlockBase):
    def __init__(self, table=None, vars=[], title='Summary Statistics'):
        self._init_block(table, title)
        self.vars(vars)
        
    # Set the summary variables
    def vars(self, vars=[]):
        if type(vars) == str:
            vars = [vars]
        self._vars = vars
        
    # Get summary variables
    def get_vars(self):
        return self._vars
        
    # Number of columns (variables)
    def ncols(self):
        return len(self._vars)

    
    
    ##########################################################################
    # Generate summary statistics
    ##########################################################################
    
    # Generate a row of summary statistics cells
    # must be assigned to a table
    def generate(self):
        self._df = self._table._vgroup_df
        self._init_row('summary')
        self._N()
        self._mean()
        self._std()
        self._pctiles()
        self._freq()
        
    # Compute count for a row of cells
    def _N(self):
        vars = self._vars
        counts = self._df.count()
        [self._row[v].N(counts[v]) for v in vars]
            
    # Compute mean for a row of cells
    def _mean(self):
        vars = [v for v in self._vars
            if self._df._vars[v]['type'] != 'category']
        means = self._df.mean()
        [self._row[v].mean(means[v]) for v in vars]
            
    # Compute standard deviation for a row of cells
    def _std(self):
        vars = [v for v in self._vars
            if self._df._vars[v]['type'] in ['binary','ordered','numeric']]
        stds = self._df[vars].std()
        [self._row[v].std(stds[v]) for v in vars]
        
    # Compute percentiles for a row of cells
    def _pctiles(self):
        vars = [v for v in self._vars
            if self._df._vars[v]['type'] == 'numeric']
        for v in vars:
            pctiles = self._df._vars[v]['cell_pctile']
            vals = self._df[v].quantile(pctiles)
            self._row[v].pctiles(list(zip(pctiles, vals)))
    
    # Compute value frequencies for a row of cells
    def _freq(self):
        vars = [v for v in self._vars
            if self._df._vars[v]['type'] in ['category','binary','ordered']]
        for v in vars:
            val_counts = self._df[v].value_counts()
            val_counts = val_counts / self._row[v]._N
            self._row[v].freq(list(zip(val_counts.data.index, val_counts)))
    
    
    
    ##########################################################################
    # Write
    ##########################################################################
    
    def _write(self, row, col):
        self._write_block(row, col, 'summary')
    
    
    
    ##########################################################################
    # Overload
    ##########################################################################
    
    # Deepcopy makes a deep copy of Summary variables
    # does not assign to memo Table or preserve cells
    def __deepcopy__(self, memo):
        return Summary(vars=deepcopy(self._vars), title=self._title)