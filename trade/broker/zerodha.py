from backtrader.brokers.bbroker import BackBroker
from backtrader.order import BuyOrder, SellOrder

from jugaad_trader import Zerodha
# kite = Zerodha()
 
# # Set access token loads the stored session.
# # Name chosen to keep it compatible with kiteconnect.
# kite.set_access_token()

# # Get profile
# profile = kite.profile()
# print(profile)

# # Get margin
# margins = kite.margins()
# print(margins)

# # Get holdings
# holdings = kite.holdings()
# print(holdings)

# # Get today's positions
# positions = kite.positions()
# print(positions)

# # Get today's orders
# orders = kite.orders()
# print(orders)

# # Finally placing an order
# order_resp = kite.place_order(variety=Zerodha.VARIETY_REGULAR,
# 			tradingsymbol="INFY",
# 			exchange=kite.EXCHANGE_NSE,
# 			transaction_type=kite.TRANSACTION_TYPE_BUY,
# 			quantity=1,
# 			order_type=kite.ORDER_TYPE_MARKET,
# 			product=kite.PRODUCT_CNC)
# print(order_resp)



class Broker(BackBroker):
    def __init__(self):
        super(Broker, self).__init__()
        self.kite = Zerodha()
        self.kite.set_access_token()
        profile = self.kite.profile()
        print(profile)

    def buy(self, owner, data,
            size, price=None, plimit=None,
            exectype=None, valid=None, tradeid=0, oco=None,
            trailamount=None, trailpercent=None,
            parent=None, transmit=True,
            histnotify=False, _checksubmit=True,tradingsymbol=None,
            **kwargs):

        order = BuyOrder(owner=owner, data=data,
                         size=size, price=price, pricelimit=plimit,
                         exectype=exectype, valid=valid, tradeid=tradeid,
                         trailamount=trailamount, trailpercent=trailpercent,
                         parent=parent, transmit=transmit,
                         histnotify=histnotify)
        
        self.place_order_kite(self.kite.TRANSACTION_TYPE_BUY, tradingsymbol, size)

        order.addinfo(**kwargs)
        self._ocoize(order, oco)

        return self.submit(order, check=_checksubmit)

    def sell(self, owner, data,
             size, price=None, plimit=None,
             exectype=None, valid=None, tradeid=0, oco=None,
             trailamount=None, trailpercent=None,
             parent=None, transmit=True,
             histnotify=False, _checksubmit=True,tradingsymbol=None,
             **kwargs):

        order = SellOrder(owner=owner, data=data,
                          size=size, price=price, pricelimit=plimit,
                          exectype=exectype, valid=valid, tradeid=tradeid,
                          trailamount=trailamount, trailpercent=trailpercent,
                          parent=parent, transmit=transmit,
                          histnotify=histnotify)
        
        self.place_order_kite(self.kite.TRANSACTION_TYPE_SELL, tradingsymbol, size)

        order.addinfo(**kwargs)
        self._ocoize(order, oco)

        return self.submit(order, check=_checksubmit)
    
    def place_order_kite(self, order_type, tradingsymbol, size):
        print(f'DUMMY ORDER PLACE {order_type}, {tradingsymbol}, {size}')
        
        # order_resp = self.kite.place_order(variety=Zerodha.VARIETY_REGULAR,
        #         tradingsymbol=tradingsymbol,
        #         exchange=self.kite.EXCHANGE_NSE,
        #         transaction_type=self.kite.TRANSACTION_TYPE_BUY,
        #         quantity=size,
        #         order_type=self.kite.ORDER_TYPE_MARKET,
        #         product=self.kite.PRODUCT_CNC)
        
        # print(order_resp)
