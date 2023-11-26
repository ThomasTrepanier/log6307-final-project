import yfinance as yf

def current_price(instrument):
    data = yf.Ticker(instrument).history(period="1d", interval="1m")
    return data["Close"].iloc[-1]

print(current_price("TSLA"))
