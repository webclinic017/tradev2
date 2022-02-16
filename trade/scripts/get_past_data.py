from yahoo_finance_api import YahooFinance

df = YahooFinance('NIFTYBEES.NS', result_range='2d', interval='1m', dropna='True').result
df = df.reset_index()
df.columns = ['date','open','high','low','close','volume']
df.to_csv('/data/projects/git_repos/tradev2/output/prod/NIFTYBEES/2022/02/15.csv', index=False)
_=123