import pandas as pd

class DFWrapper():
    def __init__(self, df=None):
        self.set_df(df)

    # Set the dataframe
    # df: pandas dataframe or None
    def set_df(self, df):
        if df is None:
            df = pd.DataFrame()
        if type(df) != pd.DataFrame:
            raise ValueError('Input must be pandas DataFrame')
        self.df = df
        
    