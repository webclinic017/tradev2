import yfinance as yf
import _initpaths

from nsetools import Nse
from trade.utils.io import write_data

import os
this_dir = os.path.dirname(os.path.abspath(__file__))

nse = Nse()

all_stock_codes = nse.get_stock_codes()
del all_stock_codes['SYMBOL']
for stock in all_stock_codes:

    ticker = yf.Ticker(f'{stock}.NS')
    print(stock)


    # ticker = yf.Ticker("INFY")

    # # get stock info
    # print(ticker.info)

    # # get historical market data
    hist = ticker.history(period="max")

    write_data(os.path.join(this_dir,f'../../data/data_yfinance_daily/{stock}.csv'), hist, index=True)

    _=123

    # # show actions (dividends, splits)
    # print(ticker.actions)

    # # show dividends
    # print(ticker.dividends)

    # # show splits
    # print(ticker.splits)

    # # show financials
    # print(ticker.financials)
    # print(ticker.quarterly_financials)

    # # show major holders
    # print(ticker.major_holders)

    # # show institutional holders
    # print(ticker.institutional_holders)

    # # show balance sheet
    # print(ticker.balance_sheet)
    # print(ticker.quarterly_balance_sheet)

    # # show cashflow
    # print(ticker.cashflow)
    # print(ticker.quarterly_cashflow)

    # # show earnings
    # print(ticker.earnings)
    # print(ticker.quarterly_earnings)

    # # show sustainability
    # print(ticker.sustainability)

    # # show analysts recommendations
    # print(ticker.recommendations)

    # # show next event (earnings, etc)
    # print(ticker.calendar)

    # # show all earnings dates
    # print(ticker.earnings_dates)

    # # show ISIN code - *experimental*
    # # ISIN = International Securities Identification Number
    # print(ticker.isin)

    # # show options expirations
    # print(ticker.options)

    # # show news
    # print(ticker.news)

    # # get option chain for specific expiration
    # opt = ticker.option_chain('2022-10-14')
    # # data available via: opt.calls, opt.puts