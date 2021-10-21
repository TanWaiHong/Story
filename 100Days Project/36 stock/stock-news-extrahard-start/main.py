import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "AC184c635820228eb7b63cf52a0a3848b0"
auth_token = "4389a7c0db4cb9d09a1913e5d2ce4fc6"

ALPHAVANTAGE_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "daily",
    "apikey": "FN2GNPKRYIYH61NE"
}

NEWS_PARAMETERS = {
    "apiKey": "10e25612f6794e089bb87db3a5428771",
    "qInTitle": COMPANY_NAME
}

alphavantage_response = requests.get(url="https://www.alphavantage.co/query", params=ALPHAVANTAGE_PARAMETERS)
alphavantage_response.raise_for_status()
data = alphavantage_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

up_down = None
if diff_percent > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

if abs(diff_percent) > -23:
    NEWS_RESPONSE = requests.get(url="https://newsapi.org/v2/everything", params=NEWS_PARAMETERS)
    NEWS_RESPONSE.raise_for_status()

    articles = NEWS_RESPONSE.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12162424248',
            to='+60192259076'
        )
        print(message.status)


