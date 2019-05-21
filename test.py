from autoanalyzer import Writer, Table, TableGenerator, Summary, Analysis
import statsmodels.api as sm
import pandas as pd

# TODO
# clean and comment
# custom DataFrame with labeling and types

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

tw = Writer(file_name='results')
tg = TableGenerator(
    table_writer=tw, title='Test title', worksheet='TestWS', df=df, 
    tgroups='SecondEstBetter', vgroups=['FirstEst', 'preference_label'])
labels = {
    'SecondEst':'Second Estimate',
    'SecondEstBetter': '% Second Estimate Preferred to First'
    }
tg.labels(labels)
tg.types({'Truth':'unary'})
summary = Summary(tg, vars=['Truth'], title='sum1')
summary = Summary(tg, vars=['SecondEstBetter', 'SecondEst'], title='sum2')
tg = TableGenerator(
    tw, title='Test title 2', worksheet='TestWS2', df=df)
tg.labels(labels)
analysis = Analysis(
    tg, y='AvgBetterPreferred', regressors=['_const'], cov_type='cluster', cov_kwds={'groups':'workerId'})
tw.write()
