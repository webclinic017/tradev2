import _initpaths
import hydra
import os
from trade.utils.cerebro_utils import get_cerebro, get_broker, get_stratergy, get_data_feed, dump_results, get_commission
this_dir = os.path.dirname(os.path.abspath(__file__))

@hydra.main(config_path=os.path.join(this_dir,'../../conf'), config_name='offline.yaml')
def my_app(config):
    # config = OmegaConf.to_object(config)
    cerebro = get_cerebro(config)

    data_feed = get_data_feed(config)
    cerebro.adddata(data_feed)

    broker = get_broker(config)
    cerebro.broker = broker

    commission = get_commission(config)
    cerebro.broker.addcommissioninfo(commission)
    
    Strategy = get_stratergy(config)
    cerebro.addstrategy(Strategy, config=config)

    cerebro.broker.setcash(config['broker']['cash'])
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    dump_results(config, cerebro)
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    _=123

if __name__ == "__main__":
    my_app()