from autoanalyzer import TableCreator
import pandas as pd

tc = TableCreator(df=pd.read_csv('data.csv'), vgroups='preference_label')
tc.set_summary(['SecondEst', 'SecondEstBetter'])
tc.set_vgroups(['FirstEst', 'preference_label'])
tc.create_table()
print(tc.sum_stats)