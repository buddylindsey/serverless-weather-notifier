import os

import arrow
import requests
from twilio.rest import Client

DARK_SKY_API_KEY = os.environ.get("DARK_SKY_API_KEY", "")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "")
TWILIO_FROM = os.environ.get("TWILIO_FROM", "")


FORCAST_URL = "https://api.darksky.net/forecast/{dark_sky_key}/{location}"

LOCATIONS = []

WEATHER_ICON = {
    "clear-day": "☀️",
    "clear-night": "🌕",
    "rain": "🌧️",
    "snow": "❄️",
    "sleet": "🌨️",
    "wind": "🌬️",
    "fog": "🌫️",
    "cloudy": "☁️",
    "partly-cloudy-day": "⛅",
    "partly-cloudy-night": "",
    "hail": "🌨️",
    "thunderstorm": "⛈️",
    "tornado": "🌪️",
}


def notify_twilio(message, number):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    data = {"body": message, "to": number, "from_": TWILIO_FROM}

    client.messages.create(**data)


def notify(event, context):
    for location in LOCATIONS:
        hour = arrow.utcnow().hour

        if hour not in location["preferred_times"]:
            continue

        forcast_data = requests.get(
            FORCAST_URL.format(
                dark_sky_key=DARK_SKY_API_KEY, location=location["location"]
            )
        ).json()

        temperature = int(forcast_data["currently"]["temperature"])
        apparent_temperature = int(forcast_data["currently"]["apparentTemperature"])
        current_icon = WEATHER_ICON[forcast_data["currently"]["icon"]]
        high = int(forcast_data["daily"]["data"][0]["temperatureMax"])
        daily_icon = WEATHER_ICON[forcast_data["daily"]["data"][0]["icon"]]
        summary = forcast_data["daily"]["data"][0]["summary"]

        message = f"Currently: {temperature}º feels like {apparent_temperature}º {current_icon}. High today: {high}º. {daily_icon} {summary}"

        notify_twilio(message, location["number"])


if __name__ == "__main__":
    notify("", "")
