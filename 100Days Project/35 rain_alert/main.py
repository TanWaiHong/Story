import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

MY_API_KEY = "36c50daa3b73ec268ebdeb5072e7d618"
CITY_ID = "1733037"
MY_CITY_LON = 101.5
MY_CITY_LAT = 3.1667
EXCLUDE_LIST = ["current", "minutely", "hourly", "daily", "alerts"]

account_sid = "AC184c635820228eb7b63cf52a0a3848b0"
auth_token = "4389a7c0db4cb9d09a1913e5d2ce4fc6"

parameters = {
    "appid": MY_API_KEY,
    "lon": MY_CITY_LON,
    "lat": MY_CITY_LAT,
    "exclude": f"{EXCLUDE_LIST[0]},{EXCLUDE_LIST[1]},{EXCLUDE_LIST[3]},{EXCLUDE_LIST[4]}"
}
weather_response = requests.get(url=OWM_ENDPOINT, params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()["hourly"]
bad_weather = False
for weather in weather_data[:12]:
    if weather["weather"][0]["id"] < 800:
        bad_weather = True
        break
if bad_weather:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella🌧️",
            from_='+12162424248',
            to='+60192259076'
        )
    print(message.status)
