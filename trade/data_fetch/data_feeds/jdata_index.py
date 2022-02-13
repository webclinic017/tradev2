import datetime as dt
import backtrader as bt
# import backtrader.feeds as btfeed

class JDataIndex(bt.feeds.GenericCSVData):
# HistoricalDate,OPEN,HIGH,LOW,CLOSE
    params = (

    # ('nullvalue', 0.0),
    ('dtformat', ('%Y-%m-%d')),
    ('datetime', 3),
    ('time', -1),
    ('high', 5),
    ('low', 6),
    ('open', 4),
    ('close', 7),
    ('volume', 8),
    ('openinterest', -1),
    ('reverse', True)
)