import yfinance as yf
import _initpaths

from nsetools import Nse
from trade.utils.io import read_data, write_data


from datetime import date
from jugaad_data.nse import stock_csv, stock_df
import pandas as pd
import multiprocessing

import os
this_dir = os.path.dirname(os.path.abspath(__file__))
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))

def process(stock):
    if os.path.exists(os.path.join(this_dir,f'../../data/data_nse_daily/{stock}.csv')):
        return
    print(stock)
    df = read_data(os.path.join(this_dir,f'../../data/data_yfinance_daily/{stock}.csv'), index=0)
    df.index = pd.to_datetime(df.index)   
    try: 
        test_df = stock_df(symbol=stock, from_date=df.index[0], to_date=df.index[-1], series="EQ").sort_index(ascending=False)
        test_df = test_df[['DATE', 'OPEN', 'HIGH', 'LOW', 'LTP','PREV. CLOSE', 'VOLUME']].set_index('DATE')
    except:
        print(stock, 'NOT FOUND')
        return
    write_data(os.path.join(this_dir,f'../../data/data_nse_daily/{stock}.csv'), test_df, index=True)

nse = Nse()

all_stock_codes = nse.get_stock_codes()
del all_stock_codes['SYMBOL']
FLAG = False


from joblib import Parallel, delayed
    
Parallel(n_jobs=1)(delayed(process)(i) for i in all_stock_codes)
    
_=123
