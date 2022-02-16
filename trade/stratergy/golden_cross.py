import math
import backtrader as bt
import datetime as dt
from trade.stratergy.base_stratergy import BaseStrategy

class Strategy(BaseStrategy):

    def __init__(self, config):
        super(Strategy, self).__init__(config)
        self.params.fast = config['stratergy']['p']['fast']
        self.params.slow = config['stratergy']['p']['slow']

        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.fast, plotname=f'{self.params.fast}-MA'
        )
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.slow, plotname=f'{self.params.slow}-MA'
        )
        self.cossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)
    
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
        
        if self.params.live:
            if dt.date.today() > self.data.datetime.date():
                return
            if dt.time(15, 30, 0) < self.data.datetime.time():
                if self.position.size > 0:
                    self.sell(size=self.size, trading_symbol=self.params.trading_symbol)
                    self.log(f'SELL {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')
                self.log('EOD Timer: Stopping strategy at eod.')
                self.cerebro.runstop()
        
        if self.position.size == 0:
            if self.cossover > 0:
                amount_to_invest = self.broker.cash*0.9
                self.size = math.floor(amount_to_invest/self.data.close[0])
                self.log(f'BUY {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')
                self.buy(size=self.size, trading_symbol=self.params.trading_symbol)

        if self.position.size > 0:
            if self.cossover < 0:
                # self.size = math.floor(amount_to_invest/self.data.close[0])
                self.sell(size=self.size, trading_symbol=self.params.trading_symbol)
                self.log(f'SELL {self.size} AT {self.data.close[0]} on {self.data.datetime.date(0)}')