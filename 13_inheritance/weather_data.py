import json
from urllib.parse import urlparse, parse_qs
from requests import Response


class InvalidURLError(Exception): ...


class CityNotFoundError(Exception): ...


WEATHER_DATA: dict = {
    "Tehran": {"main": {"temp": 283.15}},
    "London": {"main": {"temp": 280.15}},
    "New York": {"main": {"temp": 278.15}},
    "Tokyo": {"main": {"temp": 275.15}},
    "Sydney": {"main": {"temp": 290.15}},
}


def get_city_data_from_url(url: str) -> dict | None:
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)
    if "city" not in query:
        raise InvalidURLError("Invalid URL")
    city = WEATHER_DATA.get(query["city"][0])
    if city is None:
        raise CityNotFoundError("City not found")
    return city


def get_weather_data(url: str) -> Response:
    """
    fake weather api service
    sample url: http://api.fakeweathermap.org/data/2.5/weather?city=London
    """
    response = Response()
    try:
        city = get_city_data_from_url(url)
    except InvalidURLError:
        response.status_code = 400
        response._content = json.dumps({"message": "Invalid url"}).encode("utf-8")
        return response
    except CityNotFoundError:
        response.status_code = 404
        response._content = json.dumps(
            {"message": "There is no city with this name"}
        ).encode("utf-8")
        return response

    response.status_code = 200
    response._content = json.dumps(city).encode("utf-8")
    return response
