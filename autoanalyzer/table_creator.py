import pandas as pd

VTYPES = ['unary', 'binary', 'ordered', 'numeric', 'category']

class TableCreator():
    def __init__(
            self, df=None, y=None, X=None, sum_vars=None, 
            vgroups=None, hgroups=None):
        self.set_df(df)
        self.set_y(y)
        self.set_X(X)
        self.set_sum_vars(sum_vars)
        self.set_vgroups(vgroups)
        self.set_hgroups(hgroups)
        
        self.vars = {}
        self.infer_labels()
        self.infer_types()
        self.infer_group_pctiles()
        self.infer_cell_pctiles()
        
    # Set the dataframe
    # df: pandas data frame or None
    def set_df(self, df):
        if df is None:
            df = pd.DataFrame()
        if type(df) != pd.DataFrame:
            raise ValueError('Input must be pandas DataFrame')
        self.df = df
        
    # Set the y variable
    # y: string (variable name) or None
    def set_y(self, y):
        self.y = y
      
    # Set the X variables
    # X: string (variable name) or list of variable names or None
    def set_X(self, X):
        if type(X) == str:
            X = [X]
        self.X = X
        
    # Set the sum_vars variables
    # i.e. variables whose sum_vars stats are displayed in the table
    # sum_vars: string (variable name) or list of variable names or None
    def set_sum_vars(self, sum_vars):
        if type(sum_vars) == str:
            sum_vars = [sum_vars]
        self.sum_vars = sum_vars
        
    # Set the vertical groupings
    # i.e. list of vars to use as groupings along the table's vertical axis
    # vgroups: string (variable name) or list of variable names or None
    def set_vgroups(self, vgroups):
        if type(vgroups) == str:
            vgroups = [vgroups]
        self.vgroups = vgroups
        
    # Set the horizontal groupings
    # i.e. list of vars to use as groupings along the table's horizontal axis
    # hgroups: string (variable name) or list of variable names or None
    def set_hgroups(self, hgroups):
        if type(hgroups) == str:
            hgroups = [hgroups]
        self.hgroups = hgroups
        
        
        
    ###########################################################################
    # Variable decorators (lables, types, group and cell percentiles)
    ###########################################################################
        
    # Set variable labels
    # labels: {'var_name':'label'}
    def set_labels(self, labels):
        for var, label in labels.items():
            if var not in self.vars:
                self.vars[var] = {}
            self.vars[var]['label'] = label
        
    # Infer the labels of a (list of) variable(s)
    # i.e. set label to variable name
    # vars: variable name (string) or list of variable names or None
    def infer_labels(self, vars=None):
        if vars is None:
            vars = list(self.df)
        if type(vars) == str:
            vars = [vars]
        self.set_labels({var:var for var in vars})
        
    # Set variable types
    # types: {'var name':'type'}
    # type is unary, binary, ordered, numeric, or category
    def set_types(self, types):
        for var, t in types.items():
            if var not in self.vars:
                self.vars[var] = {}
            self.vars[var]['type'] = t
        
    # Infer the types (category, ordered, numeric) of a (list of) variable(s)
    # vars: variable name (string) or list of variable names or None
    # Note: variables with numeric data are inferred as ordered if the number
    # of distinct values is fewer than 10, otherwise it is inferred as numeric
    # this inference will not always be correct
    def infer_types(self, vars=None):
        if vars is None:
            vars = list(self.df)
        if type(vars) == str:
            vars = [vars]
        types = {}
        for var in vars:
            values = set(self.df[var].dropna())
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
        self.set_types(types)
        
    # Set grouping percentiles
    # i.e. percentiles to use as cutoffs when grouping by numeric variables
    # pctiles: {'var_name':[percentiles]}
    def set_group_pctiles(self, pctiles):
        self._set_pctiles(pctiles, group_pctiles=True)
            
    # Infer grouping percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_group_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=True)
        
    # Set cell percentiles
    # i.e. percentiles to use as cutoffs when displaying sum_vars stats in cell
    # pctiles: {'var_name':[percentiles]}
    def set_cell_pctiles(self, pctiles):
        self._set_pctiles(pctiles, group_pctiles=False)
        
    # Infer cell percentiles
    # vars: variable name (string) or list of variable names or None
    def infer_cell_pctiles(self, vars=None):
        self._infer_pctiles(vars, group_pctiles=False)
    
    # Set percentiles
    # pctiles: {'var_name':[percentiles]}
    # group_pctiles: indicates whether these are group or cell percentiles
    def _set_pctiles(self, pctiles, group_pctiles):
        for var, pctile in pctiles.items():
            if var not in self.vars:
                self.vars[var] = {}
            if group_pctiles:
                self.vars[var]['group_pctile'] = pctile
            else:
                self.vars[var]['cell_pctile'] = pctile
            
    # Infer percentiles
    # vars: variable name (string) or list of variable names or None
    # group_pctiles: indicates whether these are group or cell percentiles
    def _infer_pctiles(self, vars, group_pctiles):
        if vars is None:
            vars = list(self.df)
        if type(vars) == str:
            vars = [vars]
        self._set_pctiles(
            {var:[0., .25,.50,.75, 1.] for var in vars}, group_pctiles)
        
    
    
    ###########################################################################
    # Create table
    ###########################################################################
    
    # Create table
    # collect vgroup vars {vgroup: {}}
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
    def create_table(self):
        self._get_sum_stats()
        return self.sum_stats
        
    # Compute sum_vars statistics
    def _get_sum_stats(self):
        self.sum_stats = {vgroup_var: {} 
            for vgroup_var in self.vgroups+['pooled']}
        [self._get_stats_by_vgroup(vgroup_var) for vgroup_var in self.vgroups]
        self._get_stats_by_value('---', self.sum_stats['pooled'], pooled=True)
        
    # Compute sum_vars stats by vgroup variable
    # vgroup_var: from self.vgroups
    # create a series indicating membership to subgroup based on vgroup_var
    # compute sum_vars stats for each subgroup
    def _get_stats_by_vgroup(self, vgroup_var):
        if self.vars[vgroup_var]['type'] != 'numeric':
            series = self.df[vgroup_var]
        else:
            series = pd.qcut(
                self.df[vgroup_var], self.vars[vgroup_var]['group_pctile'])
                
        subgroups = series.unique()
        self.sum_stats[vgroup_var] = {sg: {} for sg in subgroups}
        [self._get_stats_by_value(sg, self.sum_stats[vgroup_var], series) 
            for sg in subgroups]
            
    # Compute sum_vars stats in subgroup
    # sg: subgroup
    # vgroup_dict: {vgroup_var: {}}
    # series: indicates membership to subgroup
    def _get_stats_by_value(self, sg, vgroup_dict, series=None, pooled=False):
        vgroup_dict[sg] = {sum_var: {} for sum_var in self.sum_vars}
        if pooled:
            temp_df = self.df
        else:
            temp_df = self.df[series==sg]
        self._N(vgroup_dict[sg], temp_df)
        self._mean(vgroup_dict[sg], temp_df)
        self._std(vgroup_dict[sg], temp_df)
        self._pctiles(vgroup_dict[sg], temp_df)
        self._counts(vgroup_dict[sg], temp_df)
        
    # Compute number of observations N
    # sg_dict: {subgroup: {sum_vars variable: {}}}
    # temp_df: df containing only members of subgroup
    def _N(self, sg_dict, temp_df):
        vars = self.sum_vars
        counts = temp_df[vars].count()
        for var in vars:
            sg_dict[var]['N'] = counts[var]
        
    def _mean(self, sg_dict, temp_df):
        vars = [v for v in self.sum_vars 
            if self.vars[v]['type'] != 'category']
        means = temp_df[vars].mean()
        for var in vars:
            sg_dict[var]['mean'] = means[var]
            
    def _std(self, sg_dict, temp_df):
        vars = [v for v in self.sum_vars
            if self.vars[v]['type'] != 'category']
        stds = temp_df[vars].std()
        for var in vars:
            sg_dict[var]['std'] = stds[var]
            
    def _pctiles(self, sg_dict, temp_df):
        vars = [v for v in self.sum_vars
            if self.vars[v]['type'] == 'numeric']
        for var in vars:
            pctiles = self.vars[var]['cell_pctile']
            vals = temp_df[var].quantile(pctiles)
            sg_dict[var]['pctiles'] = [(pctile, val) 
                for pctile, val in zip(pctiles, vals)]
                
    def _counts(self, sg_dict, temp_df):
        vars = [v for v in self.sum_vars
            if self.vars[v]['type'] != 'numeric']
        for var in vars:
            val_counts = temp_df[var].value_counts()/sg_dict[var]['N']
            sg_dict[var]['val_counts'] = list(
                zip(val_counts.index, val_counts))