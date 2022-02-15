import math
import backtrader as bt
import datetime as dt

class BaseStrategy(bt.Strategy):

    def __init__(self, config):
        self.params.live = config['live']
        self.params.trading_symbol = config['data_feed']['symbol_name']
    
    def log(self, txt):
        ''' Logging function fot this strategy'''
        date = self.datas[0].datetime.datetime(0)
        if txt==None:
            txt = f'{str(self.datas[0].open[0]):<10s}\t'+\
                    f'{str(self.datas[0].high[0]):<10s}\t'+\
                    f'{str(self.datas[0].low[0]):<10s}\t'+\
                    f'{str(self.datas[0].close[0]):<10s}\t'+\
                    f'{str(self.datas[0].volume[0]):<10s}'

        print(f'{date}\t{txt}')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None