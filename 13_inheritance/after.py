from requests import Response
from typing import Any, Protocol
from weather_data import get_weather_data


class RequestClient(Protocol):
    def get(self, url: str, timeout: int) -> Response: ...


class FakeRequestClient:
    def get(self, url: str, timeout: int) -> Response:
        response = get_weather_data(url)
        return response


class WeatherService:
    def __init__(self, city: str, request_client: RequestClient) -> None:
        self.city = city
        self.full_weather_forecast: dict[str, Any] = {}
        self.url = f"http://api.fakeweathermap.org/data/2.5/weather?city={self.city}"
        self.request_client = request_client

    def retrieve_forecast(self) -> None:
        response = self.request_client.get(self.url, timeout=5)
        if response.status_code != 200:
            raise ValueError(response.json()["message"])
        self.full_weather_forecast = response.json()

    @property
    def temperature(self):
        assert self.full_weather_forecast
        return self.full_weather_forecast["main"]["temp"] - 273.15


def main() -> None:
    city = "Tehran"
    weather_service = WeatherService(city=city, request_client=FakeRequestClient())
    weather_service.retrieve_forecast()
    print(f"The current temperature in {city} is {weather_service.temperature:.1f} °C.")


if __name__ == "__main__":
    main()
