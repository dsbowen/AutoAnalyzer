from autoanalyzer import TableWriter, Table, TableGenerator, Summary, Analysis
import statsmodels.api as sm
import pandas as pd

# TODO
# sheets
# clean and comment

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

tw = TableWriter(file_name='results')
tg = TableGenerator(
    table_writer=tw, title='Test title', df=df, 
    tgroups='SecondEstBetter', vgroups=['FirstEst', 'preference_label'])
tg.labels({
    'SecondEst':'Second Estimate',
    'SecondEstBetter': '% Second Estimate Preferred to First'})
summary = Summary(tg, vars=['Truth'], title='sum1')
summary = Summary(tg, vars=['SecondEstBetter', 'SecondEst'], title='sum2')
analysis = Analysis(tg, y='AvgBetterPreferred', regressors=['_const'], cov_type='cluster', cov_kwds={'groups':'workerId'})
tw.write()
