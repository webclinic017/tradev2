from backtrader.brokers.bbroker import BackBroker
from backtrader.order import BuyOrder, SellOrder
from trade.auth.zerodha_auth import get_kite
from jugaad_trader import Zerodha

class Broker(BackBroker):
    def __init__(self):
        super(Broker, self).__init__()
        self.kite = get_kite()

    def buy(self, owner, data,
            size, price=None, plimit=None,
            exectype=None, valid=None, tradeid=0, oco=None,
            trailamount=None, trailpercent=None,
            parent=None, transmit=True,
            histnotify=False, _checksubmit=True,trading_symbol=None,
            **kwargs):

        order = BuyOrder(owner=owner, data=data,
                         size=size, price=price, pricelimit=plimit,
                         exectype=exectype, valid=valid, tradeid=tradeid,
                         trailamount=trailamount, trailpercent=trailpercent,
                         parent=parent, transmit=transmit,
                         histnotify=histnotify)
        
        self.place_order_kite(self.kite.TRANSACTION_TYPE_BUY, trading_symbol, size)

        order.addinfo(**kwargs)
        self._ocoize(order, oco)

        return self.submit(order, check=_checksubmit)

    def sell(self, owner, data,
             size, price=None, plimit=None,
             exectype=None, valid=None, tradeid=0, oco=None,
             trailamount=None, trailpercent=None,
             parent=None, transmit=True,
             histnotify=False, _checksubmit=True,trading_symbol=None,
             **kwargs):

        order = SellOrder(owner=owner, data=data,
                          size=size, price=price, pricelimit=plimit,
                          exectype=exectype, valid=valid, tradeid=tradeid,
                          trailamount=trailamount, trailpercent=trailpercent,
                          parent=parent, transmit=transmit,
                          histnotify=histnotify)
        
        self.place_order_kite(self.kite.TRANSACTION_TYPE_SELL, trading_symbol, size)

        order.addinfo(**kwargs)
        self._ocoize(order, oco)

        return self.submit(order, check=_checksubmit)
    
    def place_order_kite(self, order_type, trading_symbol, size):
        print(f'DUMMY ORDER PLACE {order_type}, {trading_symbol}, {size}')
        
        # order_resp = self.kite.place_order(variety=Zerodha.VARIETY_REGULAR,
        #         tradingsymbol=trading_symbol,
        #         exchange=self.kite.EXCHANGE_NSE,
        #         transaction_type=order_type,
        #         quantity=size,
        #         order_type=self.kite.ORDER_TYPE_MARKET,
        #         product=self.kite.PRODUCT_CNC)
        
        # print(order_resp)