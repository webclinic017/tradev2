import backtrader as bt
import datetime as dt
class Commission(bt.CommInfoBase):

    def __init__(self):
        super().__init__()
        self.last_comission_date = dt.date.min

    def getcommission(self, size, price, order):
        '''Calculates the commission of an operation at a given price
        '''
        return self._getcommission(size, price, order, pseudoexec=True)

    def _getcommission(self, size, price, order, pseudoexec):

        if order.issell():
            order_date = order.data.datetime.date(0)
            if order_date>self.last_comission_date:
                self.last_comission_date = order_date
                return 15.93
        return 0
    
    def confirmexec(self, size, price, order):
        return self._getcommission(size, price, order, pseudoexec=True)