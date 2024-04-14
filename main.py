STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import get_price
import sys
sys.stdout.reconfigure(encoding='utf-8')
import secrets
# Now import the get_news module
import get_news
import twilio_message

percentage=get_price.get_prices()
print(percentage)
headlines=get_news.get_headlines()
for item in headlines:
    key,value=item.split(':')
    if percentage[0] >= 5:
        msg=f"""TSLA: 🔺{percentage[1]}%
        Headline:{key}. 
        Brief: {value}"""
    else:
        msg=f"""TSLA: 🔻{percentage[1]}%
        Headline:{key}. 
        Brief: {value}"""
    twilio_message.send_message(secrets.to_number,msg)

