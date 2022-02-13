import _initpaths
from trade.data_fetch.jdata import get_live_index_data
import numpy as np
import datetime as dt
import time 

while True:
    data = get_live_index_data("NIFTY 50")
    data['date'] = dt.datetime.now()
    data['last'] = data['last']+data['last'] * np.random.uniform(-0.1,0.1)
    print(data['date'], data['last'])
    time.sleep(5)

_=123