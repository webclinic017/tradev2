import _initpaths
from trade.data_fetch.data_fetcher import get_sample_data
get_sample_data()
import os
this_dir = os.path.dirname(os.path.abspath(__file__))

import backtrader as bt
import datetime as dt

cerebro = bt.Cerebro(preload=False)
cerebro.broker.setcash(2000000.0)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())




from trade.data_fetch.data_feeds.jdata_index import JDataIndex
data = JDataIndex(
    dataname=os.path.join(this_dir,'data/sample/nifty_50.csv'),
)
# data = bt.feeds.YahooFinanceCSVData(
#     dataname=os.path.join(this_dir,'data/sample/sample.csv'),
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