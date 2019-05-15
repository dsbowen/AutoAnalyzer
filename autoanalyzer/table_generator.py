##############################################################################
# Table Set
# by Dillon Bowen
# last modified 05/15/2019
##############################################################################

from autoanalyzer.table import Table
from autoanalyzer.private.table_base import TableBase
import pandas as pd

'''
Data:
    title
    df: pandas DataFrame
    tgroups: {table group variable: [group values]}
    vgroups: {vertical group variable: [group values]}
    blocks: summary and analysis blocks
    vars: {variable: {'label', 'type', 'group_pctile', 'cell pctile'}}
'''
class TableGenerator(TableBase):
    def __init__(
            self, table_writer=None, title='Untitled', df=pd.DataFrame(),
            tgroups=[], vgroups=[]):
        self.table_writer(table_writer)
        self.title(title)
        self.df(df)
        self.tgroups(tgroups)
        self.vgroups(vgroups)
        
        self._vars = {}
        self.infer_labels()
        self.infer_types()
        self.infer_group_pctiles()
        self.infer_cell_pctiles()
        
        self._blocks = []
        
    # Set table group dictionary
    # {table group variable: [group value]}
    def tgroups(self, tgroups=[]):
        self._tgroups = {t: [] for t in self._groups(tgroups)}
    
    
    
    ###########################################################################
    # Generate tables
    ###########################################################################
    
    # Generate list of tables
    def generate(self):
        self._add_constant_column()
        tables = []
        [tables.extend(self._generate_by_tgroup(t)) for t in self._tgroups]
        return tables + [self._generate_by_tgroup_val(pooled=True)]
        
    # Add constant column to dataframe
    def _add_constant_column(self):
        self._df['_const'] = 1
        self.labels({'_const': 'Constant'})
        
    # Generate list of tables split by table group variable
    def _generate_by_tgroup(self, tgroup):
        self._tgroup = tgroup
        series, values = self._get_series_values(tgroup)
        self._tgroups[tgroup] = values
        return [self._generate_by_tgroup_val(series, v) for v in values]
        
    # Generate table for a single value of the table group variable
    # analysis may be pooled over table group variable
    def _generate_by_tgroup_val(self, series=None, val=None, pooled=False):
        if pooled:
            self._tgroup = 'Pooled'
            self._tgroup_df, self._tgroup_val = self._df, None
        else:
            self._tgroup_df, self._tgroup_val = self._df[series==val], val
        return Table(self).generate()