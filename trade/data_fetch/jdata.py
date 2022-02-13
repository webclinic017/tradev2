import datetime as dt
import jugaad_data as jd
from jugaad_data.nse import index_csv, index_df
import os

from trade.utils.io import write_data
this_dir = os.path.dirname(os.path.abspath(__file__))

def get_sample_data():
    # Download as pandas dataframe
    df = jd.nse.index_df(symbol="NIFTY 50", from_date=dt.date(2010,1,1),
                to_date=dt.date.today())
    df = df.iloc[::-1]
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/sample/nifty_50.csv')
    # df = df[['HistoricalDate','OPEN','HIGH','LOW','CLOSE']]
    # df = df.rename({
    #     'HistoricalDate': 'Date',
    #     'OPEN': 'Open',
    #     'HIGH': 'High',
    #     'LOW': 'Low',
    #     'CLOSE': 'Close',
    #     }, axis=1)
    # Date,Open,High,Low,Close,Adj Close,Volume
# HistoricalDate,Index Name,INDEX_NAME,OPEN,HIGH,LOW,CLOSE

    # df = df.set_index('Date')
    # df['Adj Close'] = 1.1
    df['Volume'] = 0

    # df =
    print(df.head())
    write_data(filename, df)
    _=123