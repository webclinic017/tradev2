import yfinance as yf
import _initpaths

from nsetools import Nse
from trade.utils.io import write_data

import os
this_dir = os.path.dirname(os.path.abspath(__file__))

ticker = yf.Ticker(f'^NSEI')
hist = ticker.history(period="max")


    # ticker = yf.Ticker("INFY")

    # # get stock info
    # print(ticker.info)

    # # get historical market data

write_data(os.path.join(this_dir,f'../../data/data_yfinance_daily_nifty50/NIFTY50.csv'), hist, index=True)

_=123