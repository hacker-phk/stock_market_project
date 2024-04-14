import requests
import json
import secrets
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
def get_prices():
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={secrets.stock_key}'
    r = requests.get(url)
    jval=r.json()
    n=len(jval)
    yestarday_closing_value=float(jval["Time Series (Daily)"]["2024-04-12"]["4. close"])
    daybefore_slosing_value=float(jval["Time Series (Daily)"]["2024-04-11"]["4. close"])
    diff=yestarday_closing_value-(daybefore_slosing_value)
    pos_diff=abs(diff)
    percentage_diff=(pos_diff/daybefore_slosing_value)*100
    return [percentage_diff,diff]