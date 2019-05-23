##############################################################################
# Analysis Block
# by Dillon Bowen
# last modified 05/23/2019
##############################################################################

from autoanalyzer.bases.block_base import BlockBase
from autoanalyzer.bases.writer_base import POOLED_VAL
from copy import deepcopy
import statsmodels.api as sm
import xlsxwriter

class Analysis(BlockBase):
    def __init__(
            self, table=None, y=None, regressors=[], controls=[],
            cov_type='nonrobust', cov_kwds={}, const=True,
            title='Least Squares Regression'):
        self._init_block(table, title)
        self.y(y)
        self.regressors(regressors)
        self.controls(controls)
        self.cov_type(cov_type)
        self.cov_kwds(cov_kwds)
        self.const(const)
        
    def y(self, y=None):
        self._y = y
        
    def regressors(self, regressors=[]):
        if type(regressors) == str:
            regressors = [regressors]
        self._regressors = regressors
        
    def controls(self, controls=[]):
        if type(controls) == str:
            controls = [controls]
        self._controls = controls
        
    def cov_type(self, cov_type='nonrobust'):
        self._cov_type = cov_type
        
    def cov_kwds(self, cov_kwds={}):
        self._cov_kwds = cov_kwds
        
    def const(self, const=True):
        self._const = True
        
    def ncols(self):
        return len(self._regressors)
    
    
    
    ##########################################################################
    # Generate analysis statistics
    ##########################################################################
    
    def generate(self):
        self._init_row('analysis')
        results = self._generate_results()
        [self._row[v].param(results.params[v]) for v in self._regressors]
        [self._row[v].bse(results.bse[v]) for v in self._regressors]
        [self._row[v].tvalue(results.tvalues[v]) 
            for v in self._regressors]
        [self._row[v].pvalue(results.pvalues[v]) 
            for v in self._regressors]
        
    def _generate_results(self):
        df = deepcopy(self._table._vgroup_df)
            
        X = self._regressors + self._controls
        if self._const and '_const' not in X:
            X.append('_const')
            
        if 'groups' in self._cov_kwds:
            cov_kwds = {'groups': df[self._cov_kwds['groups']].data}
            
        return sm.OLS(df[self._y].data, df[X].data).fit(
            cov_type=self._cov_type, cov_kwds=cov_kwds)
    
    
    
    ##########################################################################
    # Write analysis statistics
    ##########################################################################
    
    def _write(self, row, col):
        self._write_block(row, col, 'analysis')