from autoanalyzer import *

# TODO
# add hgroups to Summary block
# more analyses (quantile, logit, probit, MNlogit, ordered logit/probit)
# infer analyses

df = read_csv('data.csv')
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

df.labels({
    'SecondEst': 'Second Estimate',
    'FirstEst': 'First Estimate',
    'preference_label': 'Preference question',
    'SecondEstPreferred': '% of Time Second Estimate is Preferred to First Estimate',
    'AvgBetterFirst':'% of time average estimate is better than first'})


w = Writer(file_name='results')
tg = TableGenerator(w, title='Hello world', df=df, tgroups='SecondEstPreferred', vgroups=['FirstEst', 'preference_label'])
Summary(tg, vars=['SecondEst', 'SecondEstPreferred', 'AvgBetterFirst'])
Analysis(
    tg, title='% of time average estimate is better than preferred', y='AvgBetterPreferred', regressors=['_const'], cov_type='cluster', cov_kwds={'groups':'workerId'})
w.write()
