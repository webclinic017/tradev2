from jugaad_trader import Zerodha
kite = Zerodha()
 
# Set access token loads the stored session.
# Name chosen to keep it compatible with kiteconnect.
kite.set_access_token()

# Get profile
profile = kite.profile()
print(profile)

# Get margin
margins = kite.margins()
print(margins)

# Get holdings
holdings = kite.holdings()
print(holdings)

# Get today's positions
positions = kite.positions()
print(positions)

# Get today's orders
orders = kite.orders()
print(orders)

# Finally placing an order
order_resp = kite.place_order(variety=Zerodha.VARIETY_REGULAR,
			tradingsymbol="INFY",
			exchange=kite.EXCHANGE_NSE,
			transaction_type=kite.TRANSACTION_TYPE_BUY,
			quantity=1,
			order_type=kite.ORDER_TYPE_MARKET,
			product=kite.PRODUCT_CNC)
print(order_resp)
