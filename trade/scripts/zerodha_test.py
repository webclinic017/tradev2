import _initpaths
from trade.auth.zerodha_auth import get_kite
import time
kite = get_kite()

while True:
    price = kite.quote('NSE:NIFTYBEES')['NSE:NIFTYBEES']
    date = price['timestamp']
    txt = f'{str(price["ohlc"]["open"]):<10s}\t'+\
        f'{str(price["ohlc"]["high"]):<10s}\t'+\
        f'{str(price["ohlc"]["low"]):<10s}\t'+\
        f'{str(price["last_price"]):<10s}\t'+\
        f'{str(price["volume"]):<10s}'

    print(f'{date}\t{txt}')

    # ltp = kite.ltp('NSE:NIFTYBEES')

    # print(f'')
    time.sleep(10)
# import pprint
# pprint.pprint(price)
# _=123