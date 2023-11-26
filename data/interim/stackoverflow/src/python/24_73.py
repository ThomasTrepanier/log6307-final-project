import ccxt

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'your-public-api-key',
    'secret': 'your-api-secret',
    'timeout': 30000,
    'enableRateLimit': True,
})

exchange.options = {'defaultType': 'future'}
markets = exchange.load_markets()  # Load the futures markets

for market in markets: 
    print(market)                # check for the symbol you want to trade here

# The rest of your code goes here
