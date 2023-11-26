import pandas as pd
from datetime import datetime as dt
import calendar
import io
import requests

# Yahoo history csv base url
yBase = 'https://query1.finance.yahoo.com/v7/finance/download/'
yHeaders = {
    'Accept': 'text/csv;charset=utf-8'
    }

def getYahooDf(ticker, startDate, endDate=None): # dates in ISO format
    start = dt.fromisoformat(startDate) # To datetime.datetime object
    fromDate = calendar.timegm(start.utctimetuple()) # To Unix timestamp format used by Yahoo
    if endDate is None:
        end=dt.now()
    else:
        end = dt.fromisoformat(endDate)
    toDate = calendar.timegm(end.utctimetuple())
    params = { 
        'period1': str(fromDate),
        'period2': str(toDate),
        'interval': '1d',
        'events': 'history',
        'includeAdjustedClose': 'true'
    }
    response = requests.request("GET", yBase + ticker, headers=yHeaders, params=params)
    if response.status_code < 200 or response.status_code > 299:
        return None
    else:
        csv = io.StringIO(response.text)
        df = pd.read_csv(csv, index_col='Date')
        return df
