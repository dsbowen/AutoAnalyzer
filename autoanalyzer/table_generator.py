##############################################################################
# Table Generator
# by Dillon Bowen
# last modified 05/21/2019
##############################################################################

from autoanalyzer.data_frame import DataFrame
from autoanalyzer.table import Table
from autoanalyzer.bases.table_base import TableBase

'''
Data:
    title
    df: DataFrame
    tgroups: {table group variable: [group value]}
    vgroups: {vertical group variable: [group value]}
    blocks: statistics blocks
    writer: parent Writer
'''
class TableGenerator(TableBase):
    def __init__(
            self, writer=None, worksheet=None, title='', 
            df=DataFrame(), tgroups=[], vgroups=[]):
        self.writer(writer)
        self.worksheet(worksheet)
        self.title(title)
        self.df(df)
        self.tgroups(tgroups)
        self.vgroups(vgroups)
        self._blocks = []
        
    # Set table group dictionary
    # {table group variable: [group value]}
    def tgroups(self, tgroups=[]):
        self._tgroups = {t: [] for t in self._groups(tgroups)}
        
    # Get list of table groups
    def get_tgroups(self):
        return list(self._tgroups)
    
    
    
    ##########################################################################
    # Generate tables
    ##########################################################################
    
    # Generate list of tables
    # generate tables by table group variables and pooled
    # return: [Table]
    def generate(self):
        self._decorate()
        tables = []
        [tables.extend(self._generate_by_tgroup(t)) for t in self._tgroups]
        return tables + [self._generate_by_tgroup_val(pooled=True)]
        
    # Generate list of tables split by table group variable
    # get series and values to split DataFrame
    # tgroup: table group variable
    # return: [Table]
    def _generate_by_tgroup(self, tgroup):
        self._tgroup = tgroup
        series, values = self._get_series_values(tgroup)
        self._tgroups[tgroup] = values
        return [self._generate_by_tgroup_val(series, v) for v in values]
        
    # Generate table for a single value of the table group variable
    # arguments:
    #   series: Series with split values of table group variable
    #   val: selected value of the series
    #   pooled: indicator to pool analysis over table groups
    # return: Table
    def _generate_by_tgroup_val(self, series=None, val=None, pooled=False):
        if pooled:
            self._tgroup = 'Pooled'
            self._tgroup_df, self._tgroup_val = self._df, None
        else:
            self._tgroup_df, self._tgroup_val = self._df[series==val], val
        return Table(self).generate()