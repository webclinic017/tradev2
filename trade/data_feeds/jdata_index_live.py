import datetime as dt
import backtrader as bt
from backtrader import date2num, num2date
from trade.data_fetch.jdata import get_live_index_data_line
import time
import os
this_dir = os.path.dirname(os.path.abspath(__file__))

class DataFeed(bt.feeds.GenericCSVData):


    def __init__(self, config):
        # date,open,high,low,previousClose,close,volume
        self.p.dtformat = config['data_feed']['p']['dtformat']
        self.p.datetime = config['data_feed']['p']['datetime']
        self.p.open = config['data_feed']['p']['open']
        self.p.high = config['data_feed']['p']['high']
        self.p.low = config['data_feed']['p']['low']
        self.p.close = config['data_feed']['p']['close']
        self.p.volume = config['data_feed']['p']['volume']
        self.p.time = config['data_feed']['p']['time']
        self.p.openinterest = config['data_feed']['p']['openinterest']
        self.p.reverse = config['data_feed']['p']['reverse']

    def set_index_name(self, index_name):
        self.index_name__ = index_name
        self.filename = os.path.join(
            this_dir,
            f'../data/prod/{index_name}',
            dt.date.today().strftime('%Y/%m/%d.csv')
        )
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.output_file_object = open(self.filename,'a')
        self.output_file_object.write('date,open,high,low,close,volume\n')

    def _load(self):
        if self.f is None:
            return False

        # Let an exception propagate to let the caller know
        if hasattr(self, 'index_name__'):
            line = get_live_index_data_line(self.index_name__)
            self.output_file_object.write(line)
            self.output_file_object.flush()
            time.sleep(30)
        else:
            line = self.f.readline()
            # time.sleep(1)

        if not line:
            return False

        line = line.rstrip('\n')
        linetokens = line.split(self.separator)
        return self._loadline(linetokens)
