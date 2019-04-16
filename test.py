from autoanalyzer import TableCreator
import pandas as pd

tc = TableCreator(df=pd.read_csv('data.csv'), vgroups='preference_label')
print(tc.df.head())
print(tc.vars)