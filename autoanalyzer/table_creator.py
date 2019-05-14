##############################################################################
# Table creator
# by Dillon Bowen
# last modified 05/09/2019
##############################################################################

from autoanalyzer.table import Table
import pandas as pd

VTYPES = ['unary', 'binary', 'ordered', 'numeric', 'category']

'''
Data:
    df: Pandas data frame
    y: y variable name
    X: list of X variable names
    sum_vars: list of summary statistic variable names
    vgroups: list of vertical grouping variable names
    hgroups: list of horizontal grouping variable names
    vars: {'var_name': {'type', 'label', 'cell_pctiles', 'group_pctiles'}}
'''
class TableCreator():
    def __init__(
            self, title=None, df=None, y=None, X=[], sum_vars=[], 
            vgroups=[], hgroups=[], tgroups=[]):
        self.title(title)
        self.df(df)
        self.y(y)
        self.X(X)
        self.sum_vars(sum_vars)
        self.vgroups(vgroups)
        self.hgroups(hgroups)
        self.tgroups(tgroups)
        
        self._vars = {}
        self.infer_labels()
        self.infer_types()
        self.infer_group_pctiles()
        self.infer_cell_pctiles()
        
    # Set title
    def title(self, title=None):
        self._title = title
        
    # Set the dataframe
    # df: pandas data frame or None
    def df(self, df):
        if df is None:
            df = pd.DataFrame()
        if type(df) != pd.DataFrame:
            raise ValueError('Input must be pandas DataFrame')
        self._df = df
        
    # Set the y variable
    # y: string (variable name) or None
    def y(self, y):
        self._y = y
      
    # Set the X variables
    # X: string (variable name) or list of variable names or None
    def X(self, X):
        if type(X) == str:
            X = [X]
        self._X = X
        
    # Set the sum_vars variables
    # i.e. variables whose sum_vars stats are displayed in the table
    # sum_vars: string (variable name) or list of variable names or None
    def sum_vars(self, sum_vars=[]):
        if type(sum_vars) == str:
            sum_vars = [sum_vars]
        self._sum_vars = sum_vars
        
    # Set the vertical groupings
    # i.e. list of vars to use as groupings along the table's vertical axis
    # vgroups: string (variable name) or list of variable names or None
    def vgroups(self, vgroups):
        self._vgroups = self._groups(vgroups)
        
    # Set the horizontal groupings
    # i.e. list of vars to use as groupings along the table's horizontal axis
    # hgroups: string (variable name) or list of variable names or None
    def hgroups(self, hgroups):
        self._hgroups = self._groups(hgroups)
        
    # Set the table groupings
    # i.e. list of vars to use as groupings by table
    # tgroups: string (variable name) or list of variable names or None
    def tgroups(self, tgroups):
        self._tgroups = self._groups(tgroups)
        
    # Return a list of group variable names
    def _groups(self, groups):
        if groups is None:
            return []
        if type(groups) == str:
            return [groups]
        return groups
    
        
        
    ###########################################################################
    # Variable decorators (labels, types, group and cell percentiles)
    ###########################################################################
        
    # Set variable labels
    # labels: {'var_name':'label'}
    def labels(self, labels):
        for var, label in labels.items():
            if var not in self._vars:
                self._vars[var] = {}
            self._vars[var]['label'] = label
        
    # Infer the labels of a (list of) variable(s)
    # i.e. set label to variable name
    # vars: variable name (string) or list of variable names or None
    def infer_labels(self, vars=None):
        if vars is None:
            vars = list(self._df)
        if type(vars) == str:
            vars = [vars]
        self.labels({var:var for var in vars})
        
    # Set variable types
    # types: {'var name':'type'}
    # type is unary, binary, ordered, numeric, or category
    def types(self, types):
        for var, t in types.items():
            if var not in self._vars:
                self._vars[var] = {}
            self._vars[var]['type'] = t
        
    # Infer the types (category, ordered, numeric) of a (list of) variable(s)
    # vars: variable name (string) or list of variable names or None
    # Note: variables with numeric data are inferred as ordered if the number
    # of distinct values is fewer than 10, otherwise it is inferred as numeric
    # this inference will not always be correct
    def infer_types(self, vars=None):
        if vars is None:
            vars = list(self._df)
        if type(vars) == str:
            vars = [vars]
        types = {}
        for var in vars:
            values = set(self._df[var].dropna())
            try:
                num_vals = len([float(i) for i in values])
                if num_vals == 1:
                    types[var] = 'unary'
                elif num_vals == 2:
                    types[var] = 'binary'
                elif num_vals < 10:
                    types[var] = 'ordered'
                else:
                    types[var] = 'numeric'
            except:
                types[var] = 'category'
        self.types(types)
        
    # Set grouping percentiles
    # i.e. percentiles to use as cutoffs when grouping by numeric variables
    # pctiles: {'var_name':[percentiles]}
    def group_pctiles(self, pctiles):
        self._pctiles(pctiles, group_pctiles=True)
            
    # Infer grouping percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_group_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=True)
        
    # Set cell percentiles
    # i.e. percentiles to use as cutoffs when displaying sum_vars stats in cell
    # pctiles: {'var_name':[percentiles]}
    def cell_pctiles(self, pctiles):
        self._pctiles(pctiles, group_pctiles=False)
        
    # Infer cell percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_cell_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=False)
    
    # Set percentiles
    # pctiles: {'var_name':[percentiles]}
    # group_pctiles: indicates whether these are group or cell percentiles
    def _set_pctiles(self, pctiles, group_pctiles):
        for var, pctile in pctiles.items():
            if var not in self._vars:
                self._vars[var] = {}
            if group_pctiles:
                self._vars[var]['group_pctile'] = pctile
            else:
                self._vars[var]['cell_pctile'] = pctile
            
    # Infer percentiles
    # vars: variable name (string) or list of variable names or None
    # group_pctiles: indicates whether these are group or cell percentiles
    def _infer_pctiles(self, vars, group_pctiles):
        if vars is None:
            vars = list(self._df)
        if type(vars) == str:
            vars = [vars]
        pctiles = {var:[0., .25,.50,.75, 1.] for var in vars}
        self._set_pctiles(pctiles, group_pctiles)
        
    
    
    ###########################################################################
    # Create table
    ###########################################################################
    
    # Create table
    # collect vgroup vars {vgroup_var: {}}
    # collect vgroup subgroups {vgroup_var: {sg: {}}}
    # collect sum_vars variables {vgroup_var: {sg: {sum_var: {}}}}
    # collect sum_vars stats {vgroup_var: {sg: {sum_var: {
        # mean: xxx,
        # std: xxx,
        # skewness: xxx,
        # kurtosis: xxx,
        # percentiles: {quantile_i: xxx},
        # categories: {category_i: xxx}
        # }}}}
    def create_tables(self):
        tables = []
        for tgroup_var in self._tgroups:
            self._tgroup = tgroup_var
            series, subgroups = self._get_series_subgroups(tgroup_var)
            for sg in subgroups:
                self._sg = sg
                self._tgroup_df = self._df[series==sg]
                self._compute_sum_stats()
                tables.append(Table(self))
        self._tgroup, self._sg = 'Pooled', None
        self._tgroup_df = self._df
        self._compute_sum_stats()
        tables.append(Table(self))
        return tables
        
        
    # Return a pd series containing values of subgroups and list of subgroups
    # construct series as categories or quantiles (if numeric)
    # group_var: str
    def _get_series_subgroups(self, group_var, df=None):
        if df is None:
            df = self._df
        if self._vars[group_var]['type'] == 'numeric':
            series = pd.qcut(
                df[group_var], self._vars[group_var]['group_pctile'])
        else:
            series = df[group_var]
        return (series, series.unique())
        
    # Compute sum_vars statistics
    def _compute_sum_stats(self):
        self._sum_stats = {vgroup_var: {} 
            for vgroup_var in self._vgroups+['Pooled']}
        [self._get_stats_by_vgroup(vgroup_var) for vgroup_var in self._vgroups]
        self._get_stats_by_value('---', self._sum_stats['Pooled'], Pooled=True)
        
    # Compute sum_vars stats by vgroup variable
    # vgroup_var: from self.vgroups
    # create a series indicating membership to subgroup based on vgroup_var
    # compute sum_vars stats for each subgroup
    def _get_stats_by_vgroup(self, vgroup_var):
        series, subgroups = self._get_series_subgroups(
            vgroup_var, self._tgroup_df)
        self._sum_stats[vgroup_var] = {sg: {} for sg in subgroups}
        [self._get_stats_by_value(sg, self._sum_stats[vgroup_var], series) 
            for sg in subgroups]
            
    # Compute sum_vars stats in subgroup
    # sg: subgroup
    # vgroup_dict: {vgroup_var: {}}
    # series: indicates membership to subgroup
    def _get_stats_by_value(self, sg, vgroup_dict, series=None, Pooled=False):
        vgroup_dict[sg] = {sum_var: {} for sum_var in self._sum_vars}
        if Pooled:
            self._vgroup_df = self._tgroup_df
        else:
            self._vgroup_df = self._tgroup_df[series==sg]
        self._N(vgroup_dict[sg])
        self._mean(vgroup_dict[sg])
        self._std(vgroup_dict[sg])
        self._pctiles(vgroup_dict[sg])
        self._counts(vgroup_dict[sg])
        
    # Compute number of observations N
    # sg_dict: {subgroup: {sum_vars variable: {}}}
    def _N(self, sg_dict):
        vars = self._sum_vars
        counts = self._vgroup_df[vars].count()
        for var in vars:
            sg_dict[var]['N'] = counts[var]
        
    # Compute mean
    def _mean(self, sg_dict):
        vars = [v for v in self._sum_vars 
            if self._vars[v]['type'] != 'category']
        means = self._vgroup_df[vars].mean()
        for var in vars:
            sg_dict[var]['mean'] = means[var]
        
    # Compute standard deviation
    def _std(self, sg_dict):
        vars = [v for v in self._sum_vars
            if self._vars[v]['type'] != 'category']
        stds = self._vgroup_df[vars].std()
        for var in vars:
            sg_dict[var]['std'] = stds[var]
        
    # Compute percentiles
    def _pctiles(self, sg_dict):
        vars = [v for v in self._sum_vars
            if self._vars[v]['type'] == 'numeric']
        for var in vars:
            pctiles = self._vars[var]['cell_pctile']
            vals = self._vgroup_df[var].quantile(pctiles)
            sg_dict[var]['pctiles'] = [(pctile, val) 
                for pctile, val in zip(pctiles, vals)]
            
    # Compute counts (as a percent of total N)
    def _counts(self, sg_dict):
        vars = [v for v in self._sum_vars
            if self._vars[v]['type'] != 'numeric']
        for var in vars:
            val_counts = self._vgroup_df[var].value_counts()/sg_dict[var]['N']
            sg_dict[var]['val_counts'] = list(
                zip(val_counts.index, val_counts))