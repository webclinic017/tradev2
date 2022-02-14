import datetime as dt
import backtrader as bt

class DataFeed(bt.feeds.GenericCSVData):



    params = (

    # ('nullvalue', 0.0),
    ('dtformat', ('%Y-%m-%d')),
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