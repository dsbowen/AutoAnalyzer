from autoanalyzer import TableCreator, TableWriter
import pandas as pd

tc = TableCreator(df=pd.read_csv('data.csv'), vgroups='preference_label')
tc.sum_vars(['SecondEst', 'SecondEstBetter'])
tc.vgroups(['FirstEst', 'preference_label'])
tc.y('y variable')
tc.X(['x1', 'x2'])
tw = TableWriter(file_name='results', tables=tc.create_table())
tw.write()