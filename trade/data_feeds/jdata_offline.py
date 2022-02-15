import datetime as dt
import backtrader as bt

class DataFeed(bt.feeds.GenericCSVData):
    def __init__(self, config):
        self.config = config
        self.init_params()

    def init_params(self):
        self.p.dtformat = self.config['data_feed']['p']['dtformat']
        self.p.datetime = self.config['data_feed']['p']['datetime']
        self.p.open = self.config['data_feed']['p']['open']
        self.p.high = self.config['data_feed']['p']['high']
        self.p.low = self.config['data_feed']['p']['low']
        self.p.close = self.config['data_feed']['p']['close']
        self.p.volume = self.config['data_feed']['p']['volume']
        self.p.time = self.config['data_feed']['p']['time']
        self.p.openinterest = self.config['data_feed']['p']['openinterest']
        self.p.reverse = self.config['data_feed']['p']['reverse']