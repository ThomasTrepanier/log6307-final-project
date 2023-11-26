from binance import Client
from tqdm.autonotebook import tqdm
import pandas as pd
import numpy as np

def get_binance_data(ticker, interval='4h', start='1 Jan 2018', end=None):
  client = Client()
  intervals = {
      '15m': Client.KLINE_INTERVAL_15MINUTE,
      '1h':  Client.KLINE_INTERVAL_1HOUR,      
      '4h':  Client.KLINE_INTERVAL_4HOUR,
      '1d':  Client.KLINE_INTERVAL_1DAY
  }
  interval = intervals.get(interval, '4h')
#   print(f'Historical interval {interval}')
  klines = client.get_historical_klines(symbol=ticker, interval=interval, start_str=start, end_str=end)
  data = pd.DataFrame(klines)
  data.columns = ['open_time','open', 'high', 'low', 'close', 'volume','close_time', 'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']
  data.index = [pd.to_datetime(x, unit='ms').strftime('%Y-%m-%d %H:%M:%S') for x in data.open_time]
  usecols=['open', 'high', 'low', 'close', 'volume', 'qav','num_trades','taker_base_vol','taker_quote_vol']
  data = data[usecols]
  data = data.astype('float')
  return data


client = Client()
exchange_info = client.get_exchange_info()
symbols=[s['symbol'] for s in exchange_info['symbols'] if s['status'] == 'TRADING']
ticker_list = symbols[:50]
# tiker_list = np.random.choice(symbols, size=50)
print('Number of crypto pairs: ', len(symbols))
print('First 50 pairs: ', *ticker_list)

# collect pair closes in one dataframe
coins = []
for ticker in tqdm(ticker_list):
    try:
        close_price = get_binance_data(ticker, interval='1d', start='1 Jan 2018', end='1 Jul 2022')['close'].to_dict()
        info = {'name': ticker}
        info.update(close_price)
        coins.append(info)
    except Exception as err:
        print(err)
        continue

coins = pd.DataFrame(coins)
# print(coins.head())
coins.head()
