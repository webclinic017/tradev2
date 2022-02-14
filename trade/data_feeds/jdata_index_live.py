import datetime as dt
import backtrader as bt
from backtrader import date2num, num2date
from trade.data_fetch.jdata import get_live_index_data_line
import time
import os
this_dir = os.path.dirname(os.path.abspath(__file__))

class DataFeed(bt.feeds.GenericCSVData):
    params = (
    # ('nullvalue', 0.0),
    ('dtformat', ('%Y-%m-%d %H:%M:%S')),
    ('datetime', 0),
    ('time', -1),
    ('high', 2),
    ('low', 3),
    ('open', 1),
    ('close', 4),
    ('volume', 5),
    ('openinterest', -1),
    ('reverse', True)
)
    # date,open,high,low,previousClose,close,volume
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
            time.sleep(5)
        else:
            line = self.f.readline()

        if not line:
            return False

        line = line.rstrip('\n')
        linetokens = line.split(self.separator)
        return self._loadline(linetokens)
