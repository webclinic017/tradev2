import math
import backtrader as bt
import datetime as dt

class Strategy(bt.Strategy):
    params = (('fast',40), ('slow',100), ('live',True))

    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.fast, plotname='50-MA'
        )
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.slow, plotname='200-MA'
        )
        self.cossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)
        self.endrun = False
    
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
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

    def next(self):
        if self.endrun==True:
            self.cerebro.runstop()
        print(len(self))
        if self.position.size == 0:
            if self.cossover > 0:
                amount_to_invest = self.broker.cash*0.9
                self.size = math.floor(amount_to_invest/self.data.close[0])
                print(f'BUY {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')
                self.buy(size=self.size)

        if self.position.size > 0:
            if self.cossover < 0:
                # self.size = math.floor(amount_to_invest/self.data.close[0])
                self.close(size=self.size)
                print(f'SELL {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')
        
        if self.params.live:
            if dt.time(15, 30, 0) < self.data.datetime.time():
                if self.position.size > 0:
                    self.close(size=self.size)
                    print(f'SELL {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')
                self.log('EOD Timer: Stopping strategy at eod.')
                self.endrun = True