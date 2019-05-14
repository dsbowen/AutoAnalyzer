##############################################################################
# Table Base
# by Dillon Bowen
# last modified 05/14/2019
##############################################################################

import pandas as pd

class TableBase():
    # Set table writer
    def table_writer(self, writer=None):
        try:
            self._writer._tables.remove(self)
        except:
            pass
        if writer is not None:
            writer._tables.append(self)
        self._writer = writer

    # Set main title for tables in set
    def title(self, title='Untitled'):
        self._title = title
        
    # Set dataframe
    def df(self, df=pd.DataFrame()):
        self._df = df
        
    # Set variables dict
    # {var:{label, type, group_pctiles, cell_pctiles}
    def vars(self, vars={}):
        self._vars = vars
        
    # Set vertical group variables
    # {vertical group variable: [group value]
    def vgroups(self, vgroups=[]):
        self._vgroups = {v: [] for v in self._groups(vgroups)}
        
    # Convert single group as string to list
    def _groups(self, groups):
        if type(groups) == str:
            return [groups]
        return groups
        
    # Get a series split on group variable and values of that series
    def _get_series_values(self, group):
        if self._vars[group]['type'] == 'numeric':
            series = pd.qcut(
                self._df[group], self._vars[group]['group_pctile'])
        else:
            series = self._df[group]
        return (series, series.unique())
    
    
    
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