import math
import backtrader as bt
import datetime as dt
from trade.stratergy.base_stratergy import BaseStrategy

class Strategy(BaseStrategy):

    def __init__(self, config):
        super(Strategy, self).__init__(config)
        self.yesterday_return = config['stratergy']['p']['yesterday_return']
        self.prev_close_open_return = config['stratergy']['p']['prev_close_open_return']
        self.size=1
    
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
        self.log(None)

        if dt.time(9, 16, 0) == self.data.datetime.time():
            prev_close = self.data.close[-1]
            prev_prev_close = self.data.close[-2]
            prev_return = (prev_close-prev_prev_close)*100/prev_prev_close

            curr_open = self.data.open[0]
            overnight_return = (curr_open-prev_close)*100/prev_close

            if prev_return<=self.yesterday_return and overnight_return<=self.prev_close_open_return:
                self.buy(size=self.size, trading_symbol=self.params.trading_symbol)
                self.log(f'BUY {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')

        
        if dt.time(15, 30, 0) == self.data.datetime.time():
            if self.position.size > 0:
                self.sell(size=self.size, trading_symbol=self.params.trading_symbol)
                self.log(f'SELL {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')
            # self.log('EOD Timer: Stopping strategy at eod.')