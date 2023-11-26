def Pric_Precision(price, symbol):

    return str(round(float(price),[x['pricePrecision'] for x in client.futures_exchange_info()['symbols'] if x['symbol'] == symbol][0]))


def QUN_Precision(quantity, symbol):
    return str(round(float(quantity),[x['quantityPrecision'] for x in client.futures_exchange_info()['symbols'] if x['symbol'] == symbol][0]))
