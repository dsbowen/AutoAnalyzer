##############################################################################
# Data Frame
# by Dillon Bowen
# last modified 05/22/2019
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
    
    
    
    ##########################################################################
    # Operator overload
    ##########################################################################
    
    def astype(self, type):
        return DataFrame(self._to_pandas(self).astype(type))
        
    def count(self):
        return DataFrame(self._to_pandas(self).count())
        
    def dropna(self):
        return DataFrame(self._to_pandas(self).dropna())
        
    def value_counts(self):
        return DataFrame(pd.DataFrame(self)[self.keys()[0]].value_counts())
    
    # Generic overload operation
    # convert autoanalyzer DataFrames to pandas DataFrames
    # create new DataFrame by calling function on the pandas DataFrame
    # assign variable decorations and return
    def _overload(self, f, *args, **kwargs):
        args = self._to_pandas(list(args))
        kwargs = self._to_pandas(dict(kwargs))
        df = self._to_pandas(self)
        
        if not args and not kwargs:
            out = getattr(df, f)()
        elif args and not kwargs:
            out = getattr(df, f)(*args)
        elif not args and kwargs:
            out = getattr(df, f)(**kwargs)
        else:
            out = getattr(df, f)(*args, **kwargs)
            
        if type(out) != pd.DataFrame and type(out) != pd.Series:
            return out
        df = DataFrame(out)
        df._vars = {v:self._vars[v] for v in self._vars if v in df}
        return df
        
    # Convert arguments to pandas DataFrames and Series
    def _to_pandas(self, args):
        if type(args) == DataFrame:
            keys = args.keys()
            if len(keys) == 1:
                keys = keys[0]
            return pd.DataFrame(args)[keys]
        if type(args) == list:
            return [self._to_pandas(a) for a in args]
        if type(args) == dict:
            return {k:self._to_pandas(v) for k, v in args}
        return args
        
    def __abs__(self, *args, **kwargs):
        print("__abs__")
        return self._overload('__abs__', *args, **kwargs)

    def __add__(self, *args, **kwargs):
        print("__add__")
        return self._overload('__add__', *args, **kwargs)

    def __and__(self, *args, **kwargs):
        print("__and__")
        return self._overload('__and__', *args, **kwargs)

    def __array__(self, *args, **kwargs):
        print("__array__")
        return self._overload('__array__', *args, **kwargs)

    def __array_priority__(self, *args, **kwargs):
        print("__array_priority__")
        return self._overload('__array_priority__', *args, **kwargs)

    def __array_wrap__(self, *args, **kwargs):
        print("__array_wrap__")
        return self._overload('__array_wrap__', *args, **kwargs)

    def __bool__(self, *args, **kwargs):
        print("__bool__")
        return self._overload('__bool__', *args, **kwargs)

    def __bytes__(self, *args, **kwargs):
        print("__bytes__")
        return self._overload('__bytes__', *args, **kwargs)

    def __class__(self, *args, **kwargs):
        print("__class__")
        return self._overload('__class__', *args, **kwargs)

    # def __contains__(self, *args, **kwargs):
        # print("__contains__")
        # return self._overload('__contains__', *args, **kwargs)

    def __copy__(self, *args, **kwargs):
        print("__copy__")
        return self._overload('__copy__', *args, **kwargs)

    # def __deepcopy__(self, *args, **kwargs):
        # print("__deepcopy__")
        # return self._overload('__deepcopy__', *args, **kwargs)

    def __delattr__(self, *args, **kwargs):
        print("__delattr__")
        return self._overload('__delattr__', *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        print("__delitem__")
        return self._overload('__delitem__', *args, **kwargs)

    def __dict__(self, *args, **kwargs):
        print("__dict__")
        return self._overload('__dict__', *args, **kwargs)

    def __dir__(self, *args, **kwargs):
        print("__dir__")
        return self._overload('__dir__', *args, **kwargs)

    def __div__(self, *args, **kwargs):
        print("__div__")
        return self._overload('__div__', *args, **kwargs)

    def __doc__(self, *args, **kwargs):
        print("__doc__")
        return self._overload('__doc__', *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        print("__eq__")
        return self._overload('__eq__', *args, **kwargs)

    def __finalize__(self, *args, **kwargs):
        print("__finalize__")
        return self._overload('__finalize__', *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        print("__floordiv__")
        return self._overload('__floordiv__', *args, **kwargs)

    def __format__(self, *args, **kwargs):
        print("__format__")
        return self._overload('__format__', *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        print("__ge__")
        return self._overload('__ge__', *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        print("__getitem__")
        return self._overload('__getitem__', *args, **kwargs)

    def __getstate__(self, *args, **kwargs):
        print("__getstate__")
        return self._overload('__getstate__', *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        print("__gt__")
        return self._overload('__gt__', *args, **kwargs)

    def __hash__(self, *args, **kwargs):
        print("__hash__")
        return self._overload('__hash__', *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        print("__iadd__")
        return self._overload('__iadd__', *args, **kwargs)

    def __iand__(self, *args, **kwargs):
        print("__iand__")
        return self._overload('__iand__', *args, **kwargs)

    def __ifloordiv__(self, *args, **kwargs):
        print("__ifloordiv__")
        return self._overload('__ifloordiv__', *args, **kwargs)

    def __imod__(self, *args, **kwargs):
        print("__imod__")
        return self._overload('__imod__', *args, **kwargs)

    def __imul__(self, *args, **kwargs):
        print("__imul__")
        return self._overload('__imul__', *args, **kwargs)

    def __init_subclass__(self, *args, **kwargs):
        print("__init_subclass__")
        return self._overload('__init_subclass__', *args, **kwargs)

    def __invert__(self, *args, **kwargs):
        print("__invert__")
        return self._overload('__invert__', *args, **kwargs)

    def __ior__(self, *args, **kwargs):
        print("__ior__")
        return self._overload('__ior__', *args, **kwargs)

    def __ipow__(self, *args, **kwargs):
        print("__ipow__")
        return self._overload('__ipow__', *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        print("__isub__")
        return self._overload('__isub__', *args, **kwargs)

    def __iter__(self, *args, **kwargs):
        print("__iter__")
        return self._overload('__iter__', *args, **kwargs)

    def __itruediv__(self, *args, **kwargs):
        print("__itruediv__")
        return self._overload('__itruediv__', *args, **kwargs)

    def __ixor__(self, *args, **kwargs):
        print("__ixor__")
        return self._overload('__ixor__', *args, **kwargs)

    def __le__(self, *args, **kwargs):
        print("__le__")
        return self._overload('__le__', *args, **kwargs)

    # def __len__(self, *args, **kwargs):
        # print("__len__")
        # return self._overload('__len__', *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        print("__lt__")
        return self._overload('__lt__', *args, **kwargs)

    def __matmul__(self, *args, **kwargs):
        print("__matmul__")
        return self._overload('__matmul__', *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        print("__mod__")
        return self._overload('__mod__', *args, **kwargs)

    def __module__(self, *args, **kwargs):
        print("__module__")
        return self._overload('__module__', *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        print("__mul__")
        return self._overload('__mul__', *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        print("__ne__")
        return self._overload('__ne__', *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        print("__neg__")
        return self._overload('__neg__', *args, **kwargs)

    def __nonzero__(self, *args, **kwargs):
        print("__nonzero__")
        return self._overload('__nonzero__', *args, **kwargs)

    def __or__(self, *args, **kwargs):
        print("__or__")
        return self._overload('__or__', *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        print("__pos__")
        return self._overload('__pos__', *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        print("__pow__")
        return self._overload('__pow__', *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        print("__radd__")
        return self._overload('__radd__', *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        print("__rand__")
        return self._overload('__rand__', *args, **kwargs)

    def __rdiv__(self, *args, **kwargs):
        print("__rdiv__")
        return self._overload('__rdiv__', *args, **kwargs)

    def __reduce__(self, *args, **kwargs):
        print("__reduce__")
        return self._overload('__reduce__', *args, **kwargs)

    def __reduce_ex__(self, *args, **kwargs):
        print("__reduce_ex__")
        return self._overload('__reduce_ex__', *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        print("__repr__")
        return self._overload('__repr__', *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        print("__rfloordiv__")
        return self._overload('__rfloordiv__', *args, **kwargs)

    def __rmatmul__(self, *args, **kwargs):
        print("__rmatmul__")
        return self._overload('__rmatmul__', *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        print("__rmod__")
        return self._overload('__rmod__', *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        print("__rmul__")
        return self._overload('__rmul__', *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        print("__ror__")
        return self._overload('__ror__', *args, **kwargs)

    def __round__(self, *args, **kwargs):
        print("__round__")
        return self._overload('__round__', *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        print("__rpow__")
        return self._overload('__rpow__', *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        print("__rsub__")
        return self._overload('__rsub__', *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        print("__rtruediv__")
        return self._overload('__rtruediv__', *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        print("__rxor__")
        return self._overload('__rxor__', *args, **kwargs)

    # def __setattr__(self, *args, **kwargs):
        # print("__setattr__")
        # return self._overload('__setattr__', *args, **kwargs)

    # def __setitem__(self, *args, **kwargs):
        # print("__setitem__")
        # return self._overload('__setitem__', *args, **kwargs)

    def __setstate__(self, *args, **kwargs):
        print("__setstate__")
        return self._overload('__setstate__', *args, **kwargs)

    def __sizeof__(self, *args, **kwargs):
        print("__sizeof__")
        return self._overload('__sizeof__', *args, **kwargs)

    def __str__(self, *args, **kwargs):
        print("__str__")
        return self._overload('__str__', *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        print("__sub__")
        return self._overload('__sub__', *args, **kwargs)

    def __subclasshook__(self, *args, **kwargs):
        print("__subclasshook__")
        return self._overload('__subclasshook__', *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        print("__truediv__")
        return self._overload('__truediv__', *args, **kwargs)

    def __unicode__(self, *args, **kwargs):
        print("__unicode__")
        return self._overload('__unicode__', *args, **kwargs)

    def __weakref__(self, *args, **kwargs):
        print("__weakref__")
        return self._overload('__weakref__', *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        print("__xor__")
        return self._overload('__xor__', *args, **kwargs)