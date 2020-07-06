"""Supercell Package Tests"""
# Standard Library
import unittest

# Third Party Code
import responses

# Supercell Code
import supercell


class SupercellTestSuite(unittest.TestCase):
    @responses.activate
    def test_get_nearby(self):
        responses.add(
            responses.GET,
            "https://api.weather.com/v3/location/near",
            json={},
            status=200,
        )
        nearby = supercell.get_nearby(
            longitude=39.3939, latitude=-109.109109, api_key="123456"
        )
        self.assertEqual(1, len(responses.calls))
        self.assertTrue(
            responses.calls[0].request.url.startswith(
                "https://api.weather.com/v3/location/near"
            )
        )
        print(responses.calls[0].request.params)
        self.assertEqual(
            {
                "format": "json",
                "apiKey": "123456",
                "geocode": "-109.109109,39.3939",
                "product": "postal",
            },
            responses.calls[0].request.params,
        )
        assert nearby == {}

    @responses.activate
    def test_get_forecasts(self):
        responses.add(
            responses.GET,
            "https://api.weather.com/v3/wx/forecast/daily/5day",
            json={
                "validTimeLocal": [
                    "2020-01-01T07:30:00-0600",
                    "2020-01-02T07:30:00-0600",
                    "2020-01-03T07:30:00-0600",
                    "2020-01-04T07:30:00-0600",
                    "2020-01-05T07:30:00-0600",
                ],
                "temperatureMin": [30, 31, 32, 33, 34],
                "temperatureMax": [48, 49, 50, 51, 52],
            },
        )

        forecasts = supercell.get_forecasts(
            longitude=39.3939, latitude=-109.109109, api_key="AAAbbbCCCddd"
        )

        self.assertEqual(5, len(forecasts))
        self.assertEqual(
            [(30, 48), (31, 49), (32, 50), (33, 51), (34, 52)],
            [(f.temperature_min, f.temperature_max) for f in forecasts],
        )

        self.assertEqual(1, len(responses.calls))
        self.assertTrue(
            responses.calls[0].request.url.startswith(
                "https://api.weather.com/v3/wx/forecast/daily/5day"
            )
        )
        self.assertEqual(
            {
                "geocode": "-109.109109,39.3939",
                "apiKey": "AAAbbbCCCddd",
                "format": "json",
                "language": "en-US",
                "units": "e",
            },
            responses.calls[0].request.params,
        )

    @responses.activate
    def test_get_forecasts_bad_date(self):
        responses.add(
            responses.GET,
            "https://api.weather.com/v3/wx/forecast/daily/5day",
            json={
                "validTimeLocal": [
                    "2020-01-01T07:30:00-0600",
                    "2020-01-02T07:30:00-0600",
                    "2020-01cccccccccc00-0600",
                    "2020-01-04T07:30:00-0600",
                    "2020-01-05T07:30:00",
                ],
                "temperatureMin": [30, 31, 32, 33, 34],
                "temperatureMax": [48, 49, 50, 51, 52],
            },
        )

        forecasts = supercell.get_forecasts(
            longitude=39.3939, latitude=-109.109109, api_key="AAAbbbCCCddd"
        )

        self.assertEqual(4, len(forecasts))
        self.assertEqual(
            [(30, 48), (31, 49), (33, 51), (34, 52)],
            [(f.temperature_min, f.temperature_max) for f in forecasts],
        )

        self.assertEqual(1, len(responses.calls))
        self.assertTrue(
            responses.calls[0].request.url.startswith(
                "https://api.weather.com/v3/wx/forecast/daily/5day"
            )
        )
        self.assertEqual(
            {
                "geocode": "-109.109109,39.3939",
                "apiKey": "AAAbbbCCCddd",
                "format": "json",
                "language": "en-US",
                "units": "e",
            },
            responses.calls[0].request.params,
        )

    @responses.activate
    def test_get_station_weather(self):
        responses.add(
            responses.GET,
            "https://api.weather.com/v2/pws/observations/current",
            json={
                "observations": [
                    {
                        "lat": 39.3939,
                        "lon": -109.109109,
                        "humidity": 13.2,
                        "obsTimeUtc": "2020-05-06T07:30:01",
                        "imperial": {
                            "temp": 43.2,
                            "windChill": 41.1,
                            "windSpeed": 4.0,
                            "pressure": 29.55,
                            "windGust": 5.4,
                        },
                    }
                ]
            },
        )

        observation = supercell.get_station_weather(
            station_id="AAAA1430Z", api_key="BBBcccDDDeeeFFF"
        )
        observation.identifier = 273036779480535150

        self.assertIsInstance(observation, supercell.models.Observation)
        self.assertEqual(
            {
                "humidity": 13.2,
                "latitude": 39.3939,
                "longitude": -109.109109,
                "observed_at": 1588771801.0,
                "observed_at_date": 1588723200.0,
                "observed_at_str": "2020-05-06 07:30:01",
                "observed_at_time": 730,
                "observed_at_utc_offset_seconds": 0,
                "temperature": 43.2,
                "identifier": 273036779480535150,
            },
            observation.to_dict(),
        )
