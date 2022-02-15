import backtrader as bt
from matplotlib import pyplot as plt
from trade.utils.data_util import get_result_files
import yaml

import os
this_dir = os.path.dirname(os.path.abspath(__file__))


def get_cerebro(config):
    return bt.Cerebro(
        live=config['live'],
        stdstats=config['cerebro']['stdstats'],
        oldbuysell=config['cerebro']['oldbuysell'],
        )

def get_data_feed(config):
    if config['data_feed']['name'] == 'jdata_live':
        from trade.data_feeds.jdata_live import DataFeed
        data_feed = DataFeed(
        dataname=os.path.join(this_dir,config['data_feed']['filepath']),
        timeframe=bt.TimeFrame.Seconds,
        config=config
        )
    
    if config['data_feed']['name'] == 'jdata_offline':
        from trade.data_feeds.jdata_offline import DataFeed
        data_feed = DataFeed(
        dataname=os.path.join(this_dir,config['data_feed']['filepath']),
        timeframe=bt.TimeFrame.Seconds,
        config=config
        )

    return data_feed

def get_broker(config):
    if config['broker']['name'] == 'simulator':
        from backtrader.brokers.bbroker import BackBroker as Broker

    elif config['broker']['name'] == 'zerodha':
        from trade.broker.zerodha import Broker

    return Broker

def get_stratergy(config):
    if config['stratergy']['name'] == 'golden_cross':
        from trade.stratergy.golden_cross import Strategy
    if config['stratergy']['name'] == 'test':
        from trade.stratergy.test import Strategy
    
    return Strategy

def dump_results(config, cerebro):
    filename_plot, filename_pl = get_result_files(config)
    fig = cerebro.plot()
    fig[0][0].set_size_inches(20.5, 16.5)
    plt.savefig(filename_plot, dpi=200)

    pl = {
            'start':config['broker']['cash'],
            'end': cerebro.broker.getvalue(),
            'p/l': cerebro.broker.getvalue()-config['broker']['cash']
    }

    with open(filename_pl, 'w') as outfile:
        yaml.dump(pl, outfile, default_flow_style=False)
