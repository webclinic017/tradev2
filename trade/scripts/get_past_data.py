import _initpaths
from yahoo_finance_api import YahooFinance
from trade.utils.io import write_data

df = YahooFinance('NIFTYBEES.NS', result_range='1d', interval='1m', dropna='True').result
# df = YahooFinance('NIFTYBEES.NS',result_range=None, start='01-02-2022',end='17-02-2022', interval='1m', dropna='True').result
print(df.shape)
df = df.reset_index()
df.columns = ['date','open','high','low','close','volume']
df.to_csv('/data/projects/git_repos/tradev2/output/prod/NIFTYBEES/2022/02/17.csv', index=False)

# write_data('/data/projects/git_repos/tradev2/data/NIFTYBEES/data.csv', df)
# df.to_csv(, index=False)

_=123