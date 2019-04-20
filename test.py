from autoanalyzer import TableCreator, TableWriter
import pandas as pd

tc = TableCreator(df=pd.read_csv('data.csv'), vgroups='preference_label')
tc.set_sum_vars(['SecondEst', 'SecondEstBetter'])
tc.set_vgroups(['FirstEst', 'preference_label'])
tc.create_table()
tw = TableWriter(sum_vars=tc.sum_vars, sum_stats=tc.sum_stats)
tw.write()