import _initpaths
from trade.data_fetch.jdata import get_sample_data
get_sample_data()
import os
this_dir = os.path.dirname(os.path.abspath(__file__))

import backtrader as bt
import datetime as dt

cerebro = bt.Cerebro()
# data_store = bt.store.
cerebro.broker.setcash(2000000.0)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

import backtrader as bt

# ibstore = bt.stores.IBStore(port=7496)
data = bt.feeds.IBData(dataname='EUR.USD-CASH-IDEALPRO',
                       host='127.0.0.1', port=7496, clientId=35)

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
plt.savefig('foo.png', dpi=200)
# plt.savefig('foo.pdf')

_=123