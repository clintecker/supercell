"""Supercell Package Tests"""
# Standard Library
import datetime
import unittest

# Third Party Code
from dateutil.tz import tzoffset, tzutc

# Supercell Code
import supercell


class SupercellForecastModelTestSuite(unittest.TestCase):
    def test_forecast_model(self):
        f = supercell.Forecast(
            forecast_for_date=datetime.date(2001, 10, 2),
            forecast_for_utc_offset_seconds=-21600,
            forecast_made_datetime=datetime.datetime(
                2001, 10, 1, 2, 2, 2, tzinfo=tzutc()
            ),
            temperature_min=-10,
            temperature_max=10,
            longitude=39.3939,
            latitude=-109.109109,
            identifier="aaabbbccc",
        )
        self.assertEqual(datetime.date(2001, 10, 1), f.forecast_made_date)
        self.assertEqual(1001894400.0, f.forecast_made_date_float)

        self.assertEqual(datetime.time(2, 2, 2, tzinfo=tzutc()), f.forecast_made_time)
        self.assertEqual(
            2001, f.forecast_made_year,
        )
        self.assertEqual(
            10, f.forecast_made_month,
        )
        self.assertEqual(1, f.forecast_made_day)
        self.assertEqual(2, f.forecast_made_hour)
        self.assertEqual(2, f.forecast_made_minute)
        self.assertEqual(
            0, f.forecast_made_utc_offset_seconds,
        )
        self.assertEqual(2001, f.forecast_for_year)
        self.assertEqual(10, f.forecast_for_month)
        self.assertEqual(2, f.forecast_for_day)
        self.assertEqual(
            {
                "identifier": "aaabbbccc",
                "longitude": 39.3939,
                "latitude": -109.109109,
                "forecast_made_str": "2001-10-01 02:02:02+00:00",
                "forecast_made": 1001901722.0,
                "forecast_made_date": 1001894400.0,
                "forecast_made_time": 202,
                "forecast_made_utc_offset_seconds": 0.0,
                "forecast_for_date_str": "2001-10-02",
                "forecast_for_date": 1001980800.0,
                "forecast_for_utc_offset_seconds": -21600,
                "temperature_min": -10.0,
                "temperature_max": 10.0,
            },
            f.to_dict(),
        )

    def test_forecast_model_alternate(self):
        f = supercell.Forecast(
            forecast_for_date="2001-10-02",
            forecast_for_utc_offset_seconds=-21600,
            forecast_made_datetime="2001-10-01T02:02:02-0600",
            temperature_min=-10,
            temperature_max=10,
            longitude=39.3939,
            latitude=-109.109109,
            identifier="aaabbbccc",
        )
        self.assertEqual(datetime.date(2001, 10, 1), f.forecast_made_date)
        self.assertEqual(
            datetime.time(2, 2, 2, tzinfo=tzoffset(None, -21600)), f.forecast_made_time
        )
        self.assertEqual(
            2001, f.forecast_made_year,
        )
        self.assertEqual(
            10, f.forecast_made_month,
        )
        self.assertEqual(1, f.forecast_made_day)
        self.assertEqual(2, f.forecast_made_hour)
        self.assertEqual(2, f.forecast_made_minute)
        self.assertEqual(
            -21600, f.forecast_made_utc_offset_seconds,
        )
        self.assertEqual(2001, f.forecast_for_year)
        self.assertEqual(10, f.forecast_for_month)
        self.assertEqual(2, f.forecast_for_day)
        self.assertEqual(
            {
                "identifier": "aaabbbccc",
                "longitude": 39.3939,
                "latitude": -109.109109,
                "forecast_made_str": "2001-10-01 02:02:02-06:00",
                "forecast_made": 1001923322.0,
                "forecast_made_date": 1001894400.0,
                "forecast_made_time": 202,
                "forecast_made_utc_offset_seconds": -21600,
                "forecast_for_date_str": "2001-10-02",
                "forecast_for_date": 1001980800.0,
                "forecast_for_utc_offset_seconds": -21600,
                "temperature_min": -10.0,
                "temperature_max": 10.0,
            },
            f.to_dict(),
        )

    def test_forecast_model_optionals(self):
        supercell.Forecast(
            forecast_for_date="2001-10-02",
            forecast_for_utc_offset_seconds=-21600,
            forecast_made_datetime="2001-10-01T02:02:02+0000",
            temperature_min=None,
            temperature_max=None,
            longitude=39.3939,
            latitude=-109.109109,
        )


class SupercellObservationModelTestSuite(unittest.TestCase):
    def test_observation_model(self):
        o = supercell.Observation(
            temperature=43.2,
            humidity=13,
            windchill=43.1,
            windspeed=1.2,
            pressure=29.3,
            windgust=4.2,
            longitude=39.3939,
            latitude=-109.109109,
            observed_at_str="2020-05-05 00:00:00-0600",
            identifier="aaaabbbccc",
        )
        self.assertEqual(-21600, o.observed_at_utc_offset_seconds)
        self.assertEqual(
            {
                "identifier": "aaaabbbccc",
                "longitude": 39.3939,
                "latitude": -109.109109,
                "observed_at_str": "2020-05-05 00:00:00-06:00",
                "observed_at": 1588658400.0,
                "observed_at_utc_offset_seconds": -21600,
                "observed_at_date": 1588636800.0,
                "observed_at_time": 0,
                "temperature": 43.2,
                "humidity": 13.0,
            },
            o.to_dict(),
        )
