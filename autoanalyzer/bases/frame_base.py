##############################################################################
# Base for DataFrame and Series
# by Dillon Bowen
# last modified 05/23/2019
##############################################################################

import pandas as pd

class FrameBase():
    # Generic overload operation
    # convert autoanalyzer DataFrames/Series to pandas DataFrames/Series
    # set output by calling function on the pandas DataFrame/Series
    # convert output from pandas and return
    def _overload(self, f, *args, **kwargs):
        print(args)
        print(kwargs)
        args = self._to_pandas(list(args))
        kwargs = self._to_pandas(dict(kwargs))
        print('after to pandas')
        print(args)
        print(kwargs)
        
        method = getattr(self._data, f)
        if not args and not kwargs:
            out = method()
        elif args and not kwargs:
            out = method(*args)
        elif not args and kwargs:
            out = method(**kwargs)
        else:
            out = method(*args, **kwargs)
            
        return self._from_pandas(out)
        
    # Convert arguments to pandas DataFrames and Series
    def _to_pandas(self, args):
        from autoanalyzer.data_frame import DataFrame
        from autoanalyzer.series import Series
        
        if type(args) == DataFrame or type(args) == Series:
            return args._data
        if type(args) == list:
            return [self._to_pandas(a) for a in args]
        if type(args) == dict:
            return {k:self._to_pandas(v) for k, v in args.items()}
        return args
        
    # Convert output from pandas DataFrame and Series
    def _from_pandas(self, out):
        from autoanalyzer.data_frame import DataFrame
        from autoanalyzer.series import Series
    
        if type(out) != pd.DataFrame and type(out) != pd.Series:
            return out
        if type(out) == pd.DataFrame:
            out = DataFrame(out)
        elif type(out) == pd.Series:
            out = Series(out)
        out._vars = {v:self._vars[v] for v in self._vars if v in out}
        return out