from autoanalyzer import *

# TODO
# clean and comment

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
w.write()

'''
# tw = Writer(file_name='results')
# tg = TableGenerator(
    # table_writer=tw, title='Test title', worksheet='TestWS', df=df, 
    # tgroups='SecondEstBetter', vgroups=['FirstEst', 'preference_label'])
# labels = {
    # 'SecondEst':'Second Estimate',
    # 'SecondEstBetter': '% Second Estimate Preferred to First'
    # }
# tg.labels(labels)
# tg.types({'Truth':'unary'})
# summary = Summary(tg, vars=['Truth'], title='sum1')
# summary = Summary(tg, vars=['SecondEstBetter', 'SecondEst'], title='sum2')
# tg = TableGenerator(
    # tw, title='Test title 2', worksheet='TestWS2', df=df)
# tg.labels(labels)
# analysis = Analysis(
    # tg, y='AvgBetterPreferred', regressors=['_const'], cov_type='cluster', cov_kwds={'groups':'workerId'})
# tw.write()
'''