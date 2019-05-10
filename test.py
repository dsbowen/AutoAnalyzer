from autoanalyzer import TableCreator, TableWriter
import pandas as pd

# TODO
# variable labels
# table titles
# table subgroup titles

tc = TableCreator(df=pd.read_csv('data.csv'), vgroups='preference_label')
tc.sum_vars(['SecondEst', 'SecondEstBetter'])
tc.vgroups(['FirstEst', 'preference_label'])
tc.tgroups('SecondEstBetter')
tc.y('y variable')
tc.X(['x1', 'x2'])
tw = TableWriter(file_name='results', tables=tc.create_tables())
tw.write()