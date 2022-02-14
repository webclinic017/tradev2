import _initpaths
import hydra
from omegaconf import DictConfig, OmegaConf

import os
this_dir = os.path.dirname(os.path.abspath(__file__))

import backtrader as bt
import trade.data_feeds.jdata_index_live
from matplotlib import pyplot as plt

def get_data_feed(config):
    if config['data_feed']['name'] == 'index_live':
        from trade.data_feeds.jdata_index_live import DataFeed
        data_feed = DataFeed(
        dataname=os.path.join(this_dir,config['data_feed']['filepath']),
        timeframe=bt.TimeFrame.Seconds
        )

        if config['test']==False:
            data_feed.set_index_name('NIFTY 50')
    
    return data_feed

def get_stratergy(config):
    if config['stratergy']['name'] == 'golden_cross':
        from trade.stratergy.golden_cross import Strategy
    
    return Strategy

def dump_plot(config, cerebro):
    fig = cerebro.plot()
    fig[0][0].set_size_inches(20.5, 16.5)
    plt.savefig(os.path.join(this_dir,'../foo.png'), dpi=200)

@hydra.main(config_path=os.path.join(this_dir,'../conf'), config_name='prod.yaml')
def my_app(config):
    # config = OmegaConf.to_object(config)
    cerebro = bt.Cerebro(
        live=config['cerebro']['live'],
        stdstats=config['cerebro']['stdstats'],
        oldbuysell=config['cerebro']['oldbuysell'],
        )
    
    cerebro.broker.setcash(config['broker']['cash'])
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())


    data_feed = get_data_feed(config)
    cerebro.adddata(data_feed)

    Strategy = get_stratergy(config)
    cerebro.addstrategy(Strategy)

    cerebro.run()
    dump_plot(config, cerebro)
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    _=123

if __name__ == "__main__":
    my_app()