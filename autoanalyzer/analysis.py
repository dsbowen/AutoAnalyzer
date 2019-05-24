##############################################################################
# Analysis Block
# by Dillon Bowen
# last modified 05/24/2019
##############################################################################

from autoanalyzer.bases.block_base import BlockBase
from autoanalyzer.bases.writer_base import POOLED_VAL
from copy import deepcopy
import statsmodels.api as sm
import xlsxwriter

'''
Data:
    title
    y: response variable, dependent variable, label variable
    regressors: independent variables, to be displayed in table
    controls: control variables, will not be displayed in table
    cov_type: covariance type (see statsmodels documentation)
    cov_kwds: covariance keywords (see statsmodels documentation)
    NOTE: cov_kwds refers to variable names here, but will be converted to
        pandas Series for analysis
    const: indicates constant should be included in regression
    table: parent Table
'''
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
        
    # Set dependent variable
    def y(self, y=None):
        self._y = y
        
    # Get dependent variable
    def get_y(self):
        return self._y
        
    # Set regressors
    def regressors(self, regressors=[]):
        if type(regressors) == str:
            regressors = [regressors]
        self._regressors = regressors
        
    # Get regressors
    def get_regressors(self):
        return deepcopy(self._regressors)
        
    # Set controls
    def controls(self, controls=[]):
        if type(controls) == str:
            controls = [controls]
        self._controls = controls
        
    # Get controls
    def get_controls(self):
        return deepcopy(self._controls)
        
    # Set covariance type
    def cov_type(self, cov_type='nonrobust'):
        self._cov_type = cov_type
        
    # Get covariance type
    def get_cov_type(self):
        return self._cov_type
        
    # Set covariance keywords
    def cov_kwds(self, cov_kwds={}):
        self._cov_kwds = cov_kwds
        
    # Get covariance keywords
    def get_cov_kwds(self):
        return deepcopy(self._cov_kwds)
        
    # Set indicator that constant is included in the regression
    def const(self, const=True):
        self._const = True
        
    # Get constant indicator
    def get_const(self):
        return self._const
        
    # Get the number of columns in output
    def ncols(self):
        return len(self._regressors)
    
    
    
    ##########################################################################
    # Generate analysis statistics
    ##########################################################################
    
    # Generate a row of analysis statistics cells
    # must be assigned to table
    def generate(self):
        self._init_row('analysis')
        results = self._generate_results()
        [self._row[v].param(results.params[v]) for v in self._regressors]
        [self._row[v].bse(results.bse[v]) for v in self._regressors]
        [self._row[v].tvalue(results.tvalues[v]) 
            for v in self._regressors]
        [self._row[v].pvalue(results.pvalues[v]) 
            for v in self._regressors]
        
    # Generates analysis results
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
    
    
    
    ##########################################################################
    # Operator overload
    ##########################################################################

    # Create a deep copy of analysis block
    # does not assign to parent Table or copy cells
    def __deepcopy__(self, memo):
        return Analysis(
            y=self._y, 
            regressors=deepcopy(self._regressors), 
            controls=deepcopy(self._controls),
            cov_type=self._cov_type, cov_kwds=deepcopy(self._cov_kwds), 
            const=self._const, title=self._title)