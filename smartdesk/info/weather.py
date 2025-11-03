from __future__ import annotations
import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")


class WeatherClient:
    BASE = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or OPENWEATHER_KEY
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY not set in environment or .env")

    def current_weather(self, city: str) -> dict:
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        resp = requests.get(self.BASE, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
