import _initpaths
from trade.data_fetch.data_fetcher import get_live_index_data
import numpy as np
import datetime as dt
import time 
from io import StringIO
from csv import writer 
import pandas as pd
from talib.abstract import SMA

# uses close prices (default)
# output = SMA(inputs, timeperiod=25)
# from trade.utils.io import write_data, read_data

# # live_data_df = pd.DataFrame()
# # output = StringIO()
# # csv_writer = writer(output, delimiter=',', lineterminator='\n')
# # FLAG=True
# # i=0
# # while True:
# #     i=i+1
# #     if i==10:
# #         break
# #     data = get_live_index_data("NIFTY 50")
# #     if FLAG:
# #         row = data.keys()
# #         csv_writer.writerow(row)
# #         output.flush()
# #         FLAG=False

# #     row = data.values()
# #     # for row in data:
# #     csv_writer.writerow(row)

# #     output.seek(0)
# #     live_data_df = pd.read_csv(output)
# #     print(live_data_df.tail())




# #     # return df

# #     # data['date'] = dt.datetime.now()
# #     # data['last'] = data['last']+data['last'] * np.random.uniform(-0.1,0.1)
# #     # print(data['date'], data['last'])
# #     time.sleep(60)

# import os
# from talib import stream

# filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/min_data_nifty_clean/2021/12/31.csv')
# # df['Volume'] = 0
# # write_data(filename, live_data_df)# _=123
# live_data_df = read_data(filename)

# live_data_df = stream.SMA(live_data_df['close'],timeperiod=3)


# from io import BytesIO
# from csv import writer 
# import pandas as pd

# live_data_df = pd.DataFrame({'a':[1,2,3,4]})
# output = BytesIO()
# csv_writer = writer(output)

# for row in live_data_df:
#     csv_writer.writerow(row)

# output.seek(0) # we need to get back to the start of the BytesIO
# df = pd.read_csv(output)
# # return df



import _initpaths
# from trade.data_fetch.data_fetcher import get_sample_data
# get_sample_data()
import os
this_dir = os.path.dirname(os.path.abspath(__file__))

import backtrader as bt
import datetime as dt

cerebro = bt.Cerebro(live=True,stdstats=True,oldbuysell=True)
# cerebro.addobserver(bt.observers.BuySell,barplot=True)
# cerebro.addobserver(bt.observers.Cash)
# cerebro.addobserver(bt.observers.BuySell)
# cerebro.addobserver(bt.observers.BuySell)

# strat._addobserver(False, observers.Broker)
#                     if self.p.oldbuysell:
#                         strat._addobserver(True, observers.BuySell)
#                     else:
#                         strat._addobserver(True, observers.BuySell,
#                                            barplot=True)

#                     if self.p.oldtrades or len(self.datas) == 1:
#                         strat._addobserver(False, observers.Trades)
#                     else:
#                         strat._addobserver(False, observers.DataTrades)

cerebro.broker.setcash(2000000.0)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())




from trade.data_fetch.data_feeds.jdata_index_live import JDataIndexLive
import backtrader as bt
data = JDataIndexLive(
    # dataname=os.path.join(this_dir,'data/sample/nifty_50_live.csv'),
    dataname=os.path.join(this_dir,'data/min_data_nifty_clean/2021/12/1.csv'),
    timeframe=bt.TimeFrame.Minutes

)
# data.set_index_name('NIFTY 50')

# from trade.data_fetch.data_feeds.jdata_index import JDataIndex
# data = JDataIndex(
#     dataname=os.path.join(this_dir,'data/sample/nifty_50.csv'),

# )
# data.set_index_name('NIFTY 50')


# data = bt.feeds.YahooFinanceCSVData(
#     dataname=os.path.join(this_dir,'data/sample/sample.csv'),
# )

# from trade.data_fetch.data_feeds.jdata_index import JDataIndex
# data = JDataIndex(
#     dataname=os.path.join(this_dir,'data/sample/nifty_50.csv'),
# )

cerebro.adddata(data)

from trade.stratergy.golden_cross import Strategy
# Add a strategy
cerebro.addstrategy(Strategy)

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
fig = cerebro.plot()

from matplotlib import pyplot as plt
# plt.figure(figsize=(12, 10), dpi=80)
# Plot if requested

fig[0][0].set_size_inches(30.5, 24.5)
# fig.savefig('test2png.png', dpi=100)
plt.savefig(os.path.join(this_dir,'foo.png'), dpi=200)
# plt.savefig('foo.pdf')

_=123