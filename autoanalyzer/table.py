##############################################################################
# Table
# by Dillon Bowen
# last modified 05/14/2019
##############################################################################

from autoanalyzer.private.table_base import TableBase
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
class Table(TableBase):
    def __init__(self, table_generator):
        self._title = table_generator._title
        self._vars = deepcopy(table_generator._vars)
        self.tgroup_title(table_generator._tgroup, table_generator._tgroup_val)
        self._df = table_generator._tgroup_df
        self._vgroups = deepcopy(table_generator._vgroups)
        self._blocks = []
        [b.table(self) for b in deepcopy(table_generator._blocks)]
        self._ncols = 10
        
    # Set table group title (subtitle)
    def tgroup_title(self, tgroup, tgroup_val):
        if tgroup == 'Pooled':
            self._tgroup_title = 'Pooled'
            return
        self._tgroup_title = self._vars[tgroup]['label']+' = '+str(tgroup_val)

    # Generate table statistics
    def generate(self):
        [self._generate_by_vgroup(v) for v in self._vgroups]
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
        self._vgroup_val = val
        if pooled:
            self._vgroup_df = self._df
        else:
            self._vgroup_df = self._df[series==val]
        [block.generate() for block in self._blocks]
'''
Data:
    title: str
    vars: {'var_name': {'type', 'label', 'cell_pctiles', 'group_pctiles'}}
    sum_vars: ['var_name']
    sum_stats: {'vgroup_var_name': {'subgroup': {'sum_var_name': {
        'mean': xxx,
        'std': xxx,
        'skewness': xxx,
        'kurtosis': xxx,
        'percentiles': {'quantile_i': xxx},
        'categories': {'category_i': xxx}
        }}}}
'''
'''
class Table():
    def __init__(self, table_creator):
        self.title(table_creator._title)
        self.vars(table_creator._vars)
        self.sum_vars(table_creator._sum_vars)
        self.sum_stats(table_creator._sum_stats)
        self.tgroup_title(table_creator._tgroup, table_creator._sg)
        
    # Set title
    def title(self, title):
        self._title = title
        
    # Set table group title
    # tgroup: table group variable name
    # subgroup: subgroup value
    def tgroup_title(self, tgroup, subgroup):
        if tgroup == 'Pooled':
            self._tgroup_title = 'Pooled'
            return
        self._tgroup_title = self._vars[tgroup]['label']+' = '+str(subgroup)
        
    # Set table variables
    # vars: {'var_name':{'label':label, 'type':type, '
    def vars(self, vars={}):
        self._vars = vars
        
    # Set summary variables
    def sum_vars(self, sum_vars=[]):
        self._sum_vars = sum_vars
        
    # Set summary statistics
    # sum_stats is a dict of attributes keyed by vgroup (see Data sum_stats)
    def sum_stats(self, sum_stats={}):
        self._sum_stats = sum_stats
'''