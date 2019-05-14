from autoanalyzer import TableWriter, Table, TableGenerator, Summary, Analysis
import statsmodels.api as sm
import pandas as pd

# TODO
# assign children to parents: i.e. TableSet and Table should have TableWriter
# summary block and write to file
# analysis block and write to file
# tw = TableWriter()
# ts = TableSet(tw, tgroup='SecondEstPreferred', vgroup='Question')
# summary = Summary(ts, title, [summary variables])
# analysis = Analysis(ts, title, y, [regressors], [controls], cov_type, cov_kwds, cons=True)
# tg.generate()
# tw.write()

tw = TableWriter(file_name='results')
tg = TableGenerator(
    table_writer=tw, title='Test title', df=pd.read_csv('data.csv'), 
    tgroups='SecondEstBetter', vgroups=['FirstEst', 'preference_label'])
summary = Summary(tg, vars=['Truth'], title='sum1')
summary = Summary(tg, vars=['SecondEstBetter', 'SecondEst'], title='sum2')
print(tg._blocks)
[print(t._blocks) for t in tg.generate()]
tw.write()
print(tw._vgroup_index)

'''
df = pd.read_csv('data.csv')
df['FirstEstDeviation'] = abs(df['FirstEst'] - df['Truth'])
df['AvgEst'] = (df['FirstEst'] + df['SecondEst']) / 2
df['AvgEstDeviation'] = abs(df['AvgEst'] - df['Truth'])
df['AvgBetterFirst'] = (
    df['AvgEstDeviation'] < df['FirstEstDeviation']).astype(int)
df['SecondEstPreferred'] = df['SecondEstBetter']
df['PreferredEst'] = (
    df['FirstEst'] * ~df['SecondEstPreferred'].astype(bool)
    + df['SecondEst'] * df['SecondEstPreferred'])
df['PreferredEstDeviation'] = abs(df['PreferredEst'] - df['Truth'])
df['AvgBetterPreferred'] = (
    df['AvgEstDeviation'] < df['PreferredEstDeviation']).astype(int)

df['_const'] = pd.DataFrame.from_dict({'_const':[1]*len(df)})

print(sum(df.AvgBetterPreferred)/len(df))
results = sm.OLS(df['AvgBetterPreferred'], df['_const']).fit(hasconst=True, cov_type='cluster', cov_kwds={'groups':df['workerId']})
print(resultg.summary())

print(resultg.bse)
print(resultg.fvalue, resultg.f_pvalue)
print(resultg.pvalues)
print(resultg.rsquared)
print(resultg.params)
print('t', resultg.tvalues)
'''

# Analysis:
# y, regressors, controls, cov_type, cov_kwds, title
# store: params, bse, tvalues, pvalues for regressors

# Table has vgroup variables, group values associated with each vgroup var,
# blocks of summary stats/analyses associated with a single groups
# SummaryStatsBlock, AnalysisBlock

# TableCreator takes list of tgroup variables, list of vgroup variables, list of Blocks
# for autoanalysis, TableCreator can take y, regressors, controls
# SummaryBlock takes list of variables, title (optional)
# AnalysisBlock takes y, regressors, controls, cov_type, cov_kwds, title (optional)
# TableCreator splots by vgroup value, then computes each row
# Blocks have a compute(df) method which returns 
# Table 

# TableWriter
# TableWriter.write()
# TableSet
# TableSet.table_writer(tw)
# TableSet.generate()
# Table
# df, y, regressors, controls, title, tgroups, vgroups, {vgroup: val}, ncolumns, {var: label, type}
# Blocks (Summary, Analysis)
# Summary.table_set(ts)
# Summary.compute()
# df, y, regressors, controls, variables, title

# tc = TableCreator(title='Summary Statistics', df=df)
# tc.sum_vars(['SecondEst', 'SecondEstBetter', 'AvgEst'])
# tc.vgroups(['FirstEst', 'preference_label'])
# tc.tgroups('SecondEstBetter')
# tc.labels({
    # 'FirstEst':'First Estimate',
    # 'SecondEst':'Second Estimate',
    # 'AvgEst':'Average Estimate',
    # 'preference_label':'Preference Question',
    # 'SecondEstBetter':'% of time second estimate is preferred to first'
    # })
# tw = TableWriter(file_name='results', tables=tc.create_tables())
# tw.write()

