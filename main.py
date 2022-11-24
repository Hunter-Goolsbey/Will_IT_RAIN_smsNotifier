
import requests
import os
from twilio.rest import Client

account_sid = "AC01dac300deceb117e74eb2c8e08a22f0"
auth_token = os.environ.get("AUTH_TOKEN")
num = os.environ.get("SYS_NUM")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 47.659000,
    "lon": -117.425018,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data)
weather_slice = weather_data
#print(weather_slice)

condition_code = weather_data['weather'][0]['id']
will_rain = False
if int(condition_code) <= 701:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_=num,
        to=os.environ.get("PHONE_NUM")
    )
    print(message.status)
