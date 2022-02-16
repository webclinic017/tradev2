import datetime as dt
import time
import jugaad_data as jd
from jugaad_data.nse import index_csv, index_df
import os

from trade.utils.io import write_data
this_dir = os.path.dirname(os.path.abspath(__file__))

from jugaad_data.nse import NSELive
from trade.auth.zerodha_auth import ZerodhaAuth

n = NSELive()

def get_sample_data():
    # Download as pandas dataframe
    df = jd.nse.index_df(symbol="NIFTY 50", from_date=dt.date(2010,1,1),
                to_date=dt.date.today())
    df = df.iloc[::-1]
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/sample/nifty_50.csv')
    df['volume'] = 0
    df = df.rename({'HistoricalDate':'date'}, axis=1)
    df.columns = map(str.lower,df.columns)
    df = df[['date','open','high','low','close','volume']]
    write_data(filename, df)

def get_live_index_data(index_name):
    index_price = n.live_index(index_name)

    index_price_clean = {
        "date":dt.datetime.strptime(index_price['metadata']['timeVal'], '%d-%b-%Y %H:%M:%S'),
        "open":float(index_price['metadata']['open']),
        "high":float(index_price['metadata']['high']),
        "low":float(index_price['metadata']['low']),
        # "previousClose":float(index_price['metadata']['previousClose']),
        "close":float(index_price['metadata']['last']),
        "volume":int(index_price['metadata']['totalTradedVolume']),
    }
    return index_price_clean

def get_live_index_data_line(index_name):
    index_price = n.live_index(index_name)

    index_price_clean = {
        "date":dt.datetime.strptime(index_price['metadata']['timeVal'], '%d-%b-%Y %H:%M:%S'),
        "open":float(index_price['metadata']['open']),
        "high":float(index_price['metadata']['high']),
        "low":float(index_price['metadata']['low']),
        # "previousClose":float(index_price['metadata']['previousClose']),
        "close":float(index_price['metadata']['last']),
        "volume":int(index_price['metadata']['totalTradedVolume']),
    }
    return ','.join(map(str, index_price_clean.values()))+'\n'

def get_live_symbol_data_line(symbol_name):
    
    # TODO verify that time of both price and trade_info in sync

    while True:
        try:
            price = n.stock_quote(symbol_name)
            trade_info = n.trade_info(symbol_name)
            price_clean = {
                "date":dt.datetime.strptime(price['metadata']['lastUpdateTime'], '%d-%b-%Y %H:%M:%S'),
                "open":float(price['priceInfo']['open']),
                "high":float(price['priceInfo']['intraDayHighLow']['max']),
                "low":float(price['priceInfo']['intraDayHighLow']['min']),
                # "previousClose":float(price['metadata']['previousClose']),
                "close":float(price['priceInfo']['lastPrice']),
                "volume":int(trade_info['marketDeptOrderBook']['tradeInfo']['totalTradedVolume']),
            }
            break
        except:
            time.sleep(1)
            continue

    return ','.join(map(str, price_clean.values()))+'\n'

def get_live_symbol_data_line_zerodha(symbol_name):
    
    kite = ZerodhaAuth.get_kite()

    while True:
        try:
            price = kite.quote(f'NSE:{symbol_name}')[f'NSE:{symbol_name}']

            price_clean = {
                "date":price['timestamp'],
                "open":float(price['ohlc']['open']),
                "high":float(price['ohlc']['high']),
                "low":float(price['ohlc']['low']),
                # "previousClose":float(price['metadata']['previousClose']),
                "close":float(price['last_price']),
                "volume":int(price["volume"]),
            }
            break

        except:
            time.sleep(1)
            continue

    return ','.join(map(str, price_clean.values()))+'\n'