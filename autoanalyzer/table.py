##############################################################################
# Table
# by Dillon Bowen
# last modified 05/13/2019
##############################################################################

class Table():
    def __init__(self, table_set):
        self.title(table_set._title)
        self.vars(table_set._vars)
        self.tgroup_title(table_set._tgroup, table_set._tgroup_val)
        self._vars = table_set._vars
        self._vgroups = table_set._vgroups
        self._ncols = 10
        
    # Set main table title
    def title(self, title='Untitled'):
        self._title = title
        
    # Set variables dict
    # {var:{label, type, group_pctiles, cell_pctiles}
    def vars(self, vars={}):
        self._vars = vars
        
    # Set table group title (subtitle)
    def tgroup_title(self, tgroup, tgroup_val):
        if tgroup == 'Pooled':
            self._tgroup_title = 'Pooled'
            return
        self._tgroup_title = self._vars[tgroup]['label']+' = '+str(tgroup_val)

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