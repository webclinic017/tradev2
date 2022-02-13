import datetime as dt
import jugaad_data as jd
from jugaad_data.nse import index_csv, index_df
import os

from trade.utils.io import write_data
this_dir = os.path.dirname(os.path.abspath(__file__))

from jugaad_data.nse import NSELive



def get_sample_data():
    # Download as pandas dataframe
    df = jd.nse.index_df(symbol="NIFTY 50", from_date=dt.date(2010,1,1),
                to_date=dt.date.today())
    df = df.iloc[::-1]
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/sample/nifty_50.csv')
    df['Volume'] = 0
    write_data(filename, df)

def get_live_index_data(index_name):
    n = NSELive()
    index_price = n.live_index(index_name)

    index_price_clean = {
        "date":dt.datetime.strptime(index_price['metadata']['timeVal'], '%d-%b-%Y %H:%M:%S'),
        "open":float(index_price['metadata']['open']),
        "high":float(index_price['metadata']['high']),
        "low":float(index_price['metadata']['low']),
        "previousClose":float(index_price['metadata']['previousClose']),
        "last":float(index_price['metadata']['last']),
        "volume":int(index_price['metadata']['totalTradedVolume']),
    }
    return index_price_clean