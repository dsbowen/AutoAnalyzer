##############################################################################
# Data Frame
# by Dillon Bowen
# last modified 05/21/2019
##############################################################################

import pandas as pd

# Create DataFrame from csv
def read_csv(csv):
    return DataFrame(pd.read_csv(csv))

'''
Data:
    vars: {var: {'label', 'type', 'group_pctiles', 'cell_pctiles'}}
'''
class DataFrame(pd.DataFrame):
    _vars = {}
    
    
    
    ##########################################################################
    # Decorate the dataframe
    ##########################################################################
    
    # Automatically decorate the dataframe
    def decorate(self, vars=None):
        self.infer_labels(vars)
        self.infer_types(vars)
        self.infer_group_pctiles(vars)
        self.infer_cell_pctiles(vars)
        
    # Clear decoration
    def clear_decoration(self, vars=None):
        if vars is None:
            self._vars = {}
            return
        for v in vars:
            self.vars[v] = {}
    
    
    ##########################################################################
    # Variable labels
    ##########################################################################
    
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
            vars = self._undecorated_vars('label')
        if type(vars) == str:
            vars = [vars]
        self.labels({v:v for v in vars})
        
    # Get labels
    # return {var: label}
    def get_labels(self):
        return self._decorated_vars('label')
        
    # Clear labels
    def clear_labels(self):
        self._clear_attr('label')
        
    
    
    ##########################################################################
    # Variable types
    ##########################################################################
    
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
            vars = self._undecorated_vars('type')
        if type(vars) == str:
            vars = [vars]
        types = {}
        for var in vars:
            values = set(self[var].dropna())
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
        
    # Get types
    # return: {var: type}
    def get_types(self):
        return self._decorated_vars('type')
        
    # Clear types
    def clear_types(self):
        self._clear_attr('type')
    
    
    
    ##########################################################################
    # Variable percentiles (for groupings and cells)
    ##########################################################################
    
    # Set grouping percentiles
    # i.e. percentiles to use as cutoffs when grouping by numeric variables
    # pctiles: {var: [percentile]}
    def group_pctiles(self, pctiles):
        self._set_pctiles(pctiles, group_pctiles=True)
            
    # Infer grouping percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_group_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=True)
        
    # Get group percentiles
    # return: {var: [group percentile]}
    def get_group_pctiles(self):
        return self._decorated_vars('group_pctile')
        
    # Clear group percentiles
    def clear_group_pctiles(self):
        self._clear_attr('group_pctile')
        
        
    # Set cell percentiles
    # i.e. percentiles to use as cutoffs when displaying sum_vars stats in cell
    def cell_pctiles(self, pctiles):
        self._set_pctiles(pctiles, group_pctiles=False)
        
    # Infer cell percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_cell_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=False)
        
    # Get cell percentiles
    # return: {var: [cell_pctile]}
    def get_cell_pctiles(self):
        return self._decorated_vars('cell_pctile')
        
    # Clear cell percentiles
    def clear_cell_pctiles(self):
        self._clear_attr('cell_pctile')
    
    
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
        if vars is None and group_pctiles:
            vars = self._undecorated_vars('group_pctile')
        if vars is None and not group_pctiles:
            vars = self._undecorated_vars('cell_pctile')
        if type(vars) == str:
            vars = [vars]
            
        pctiles = {var:[0., .25,.50,.75, 1.] for var in vars}
        self._set_pctiles(pctiles, group_pctiles)
    
    
    
    ##########################################################################
    # Auxiliary functions
    ##########################################################################
    
    # Return a list of variables with attribute (attr) decoration
    def _decorated_vars(self, attr):
        return {v:self._vars[v][attr] for v in self._vars 
            if attr in self._vars[v] and self._vars[v][attr] is not None}
        
    # Return a list of variables without attribute (attr) decoration
    def _undecorated_vars(self, attr):
        return [v for v in self 
            if (v not in self._vars 
            or attr not in self._vars[v] 
            or self._vars[v][attr] is None)]
            
    # Clear decoration for an attribute
    def _clear_attr(self, attr):
        for v in self._decorated_vars(attr):
            self._vars[v][attr] = None