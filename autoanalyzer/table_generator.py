##############################################################################
# Table Set
# by Dillon Bowen
# last modified 05/13/2019
##############################################################################

from autoanalyzer.table import Table
import pandas as pd

class TableGenerator():
    def __init__(
            self, title='Untitled', df=pd.DataFrame(), tgroups=[], vgroups=[]):
        self.title(title)
        self.df(df)
        self.tgroups(tgroups)
        self.vgroups(vgroups)
        
        self._vars = {}
        self.infer_labels()
        self.infer_types()
        self.infer_group_pctiles()
        self.infer_cell_pctiles()
        
    # Set main title for tables in set
    def title(self, title='Untitled'):
        self._title = title
        
    # Set dataframe
    def df(self, df=pd.DataFrame()):
        self._df = df
        
    # Set table group dictionary
    # {table group variable: [group value]}
    def tgroups(self, tgroups=[]):
        self._tgroups = {t: [] for t in self._groups(tgroups)}
        
    # Set vertical group variables
    def vgroups(self, vgroups=[]):
        self._vgroups = {v: [] for v in self._groups(vgroups)}
        
    # Convert single group as string to list
    def _groups(self, groups):
        if type(groups) == str:
            return [groups]
        return groups
        
    
    
    ###########################################################################
    # Variable decorators (labels, types, group and cell percentiles)
    ###########################################################################
        
    # Set variable labels
    # labels: {var: label}
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
    # types: {var: type}
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
    # pctiles: {var: [percentile]}
    def group_pctiles(self, pctiles):
        self._pctiles(pctiles, group_pctiles=True)
            
    # Infer grouping percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_group_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=True)
        
    # Set cell percentiles
    # i.e. percentiles to use as cutoffs when displaying sum_vars stats in cell
    def cell_pctiles(self, pctiles):
        self._pctiles(pctiles, group_pctiles=False)
        
    # Infer cell percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_cell_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=False)
    
    # Set percentiles
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
    # Generate tables
    ###########################################################################
    
    # Generate list of tables
    def generate(self):
        tables = []
        [tables.extend(self._generate_by_tgroup(t)) for t in self._tgroups]
        return tables + [self._generate_by_tgroup_val(pooled=True)]
        
    # Generate list of tables split by table group variable
    def _generate_by_tgroup(self, tgroup):
        self._tgroup = tgroup
        series, values = self._get_series_values(tgroup, self._df)
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
        [self._generate_by_vgroup(v) for v in self._vgroups]
        self._generate_by_vgroup_val(pooled=True)
        return Table(self)
        
    # Generate statistics split by vertical group variable
    def _generate_by_vgroup(self, vgroup):
        self._vgroup = vgroup
        series, values = self._get_series_values(vgroup, self._tgroup_df)
        values = sorted(list(values))
        self._vgroups[vgroup] = values
        [self._generate_by_vgroup_val(series, v) for v in values]
        
    # Generate statistics for a single value of the vertical group variable
    def _generate_by_vgroup_val(self, series=None, val=None, pooled=False):
        if pooled:
            self._vgroup_df = self._tgroup_df
        else:
            self._vgroup_df = self._tgroup_df[series==val]
        # COMPUTE BLOCK STATISTICS HERE
        
    # Get a series split on group variable and values of that series
    def _get_series_values(self, group, df):
        if self._vars[group]['type'] == 'numeric':
            series = pd.qcut(
                df[group], self._vars[group]['group_pctile'])
        else:
            series = df[group]
        return (series, series.unique())