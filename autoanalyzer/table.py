##############################################################################
# Table
# by Dillon Bowen
# last modified 05/09/2019
##############################################################################

'''
Data:
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
class Table():
    def __init__(self, vars={}, sum_vars=[], sum_stats={}):
        self.vars(vars)
        self.sum_vars(sum_vars)
        self.sum_stats(sum_stats)
        
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