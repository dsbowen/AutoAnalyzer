import pandas as pd

class TableCreator():
    def __init__(
            self, df=None, y=None, X=None, additional=None, 
            vgroups=None, hgroups=None):
        self.set_df(df)
        self.set_y(y)
        self.set_X(X)
        self.set_additional(additional)
        self.set_vgroups(vgroups)
        self.set_hgroups(hgroups)
        self.vars = {}
        self.infer_labels()
        self.infer_types()
        
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
        
    # Set the additional variables
    # i.e. variables whose summary stats are displayed in the table
    # additional: string (variable name) or list of variable names or None
    def set_additional(self, additional):
        if type(additional) == str:
            additional = [additional]
        self.additional = additional
        
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
    # Variable labels and types
    ###########################################################################
        
    # Set the labels for a (list of) variable(s)
    def set_labels(self, vars, labels):
        if type(vars) == str:
            vars = [vars]
        for var, label in zip(vars, labels):
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
        self.set_labels(vars, vars)
        
    # Set the types for a (list of) variable(s)
    # types are category, binary, ordered, numeric
    def set_types(self, vars, types):
        if type(vars) == str:
            vars = [vars]
        for var, t in zip(vars, types):
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
        types = []
        for v in vars:
            values = set(self.df[v].dropna())
            try:
                [float(i) for i in values]
                if len(values) == 2:
                    types.append('binary')
                elif len(values) < 10:
                    types.append('ordered')
                else:
                    types.append('numeric')
            except:
                types.append('category')
        self.set_types(vars, types)