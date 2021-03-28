"""Cool"""
# Standard Library
import datetime
import unittest

# Third Party Code
from bitstring import BitStream
from dateutil.tz import tzlocal

# Supercell Code
from supercell import weatherlink


class SupercellWeatherlinkModelsTestSuite(unittest.TestCase):
    RECORD_BYTES = (
        b"LOO\xc4\x00\x1d\x01\xe2r~\x03\x12\xf3\x02\x05\x07\xcf\x00"
        b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
        b"\xff$\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x7f\x00"
        b"\x00\xff\xff\x00\x00\x04\x00^\x01\x00\x00\x00\x00\x00\x00"
        b"\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x03\x07\xad"
        b"\x17\x02\xea\x07\n\r\xf3\x7f"
    )
    BAD_CRC_BYTES = (
        b"LOO\xc4\x00\x1d\x01\xe2r~\xaa\x12\xf3\x02\x05\x07\xcf"
        b"\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
        b"\xff\xff\xff$\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff"
        b"\xff\x7f\x00\x00\xff\xff\x00\x00\x04\x00^\x01\x00\x00"
        b"\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x005\x03\x07\xad\x17\x02\xff\x07\n\r\xf3\x7f"
    )
    WRONG_SIZE_BYTES = (
        b"LOO\xc4\x00\x1d\x01\xe2r~\xaa\x12\xf3\x02\x05\x07\xcf"
        b"\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
        b"\xff\xff\xff$\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff"
        b"\xff\x7f\x00\x00\xff\xff\x00\x00\x04\x00^\x01\x00\x00"
        b"\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\x00\x00"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        b"\x00\x00\x005\x03\x07\xad\x17\x02\xff\x07\n\r\xf3\x7f"
        b"\xff"
    )

    def test__wind_direction_text(self):
        t = [
            (-34, None, ValueError),
            (0, "N", None),
            (9, "N", None),
            (10, "NNE", None),
            (36, "NE", None),
            (45, "NE", None),
            (185, "S", None),
            (191, "SSW", None),
            (326, "NNW", None),
            (355, "N", None),
            (360, "N", None),
            (361, None, ValueError),
        ]
        for wind_direction, wind_direction_text, exc in t:
            if wind_direction_text:
                self.assertEqual(
                    wind_direction_text,
                    weatherlink.models._wind_direction_text(wind_direction),
                    wind_direction,
                )
            elif exc:
                with self.assertRaises(exc):
                    weatherlink.models._wind_direction_text(wind_direction)

    def test__forecast_icons_text(self):
        t = [
            (-11, None, ValueError),
            (0, [], None),
            (1, ["Rain within 12 hrs"], None),
            (2, ["Cloudy"], None),
            (3, ["Rain within 12 hrs", "Cloudy"], None),
            (4, ["Cloud + Sunny"], None),
            (5, ["Rain within 12 hrs", "Cloud + Sunny"], None),
            (6, ["Cloudy", "Cloud + Sunny"], None),
            (7, ["Rain within 12 hrs", "Cloudy", "Cloud + Sunny"], None),
            (8, ["Sunny"], None),
            (9, ["Rain within 12 hrs", "Sunny"], None),
            (10, ["Cloudy", "Sunny"], None),
            (11, ["Rain within 12 hrs", "Cloudy", "Sunny"], None),
            (12, ["Cloud + Sunny", "Sunny"], None),
            (13, ["Rain within 12 hrs", "Cloud + Sunny", "Sunny"], None),
            (14, ["Cloudy", "Cloud + Sunny", "Sunny"], None),
            (15, ["Rain within 12 hrs", "Cloudy", "Cloud + Sunny", "Sunny"], None),
            (16, ["Snow within 12hrs"], None),
            (17, ["Rain within 12 hrs", "Snow within 12hrs"], None),
            (18, ["Cloudy", "Snow within 12hrs"], None),
            (19, ["Rain within 12 hrs", "Cloudy", "Snow within 12hrs"], None),
            (20, ["Cloud + Sunny", "Snow within 12hrs"], None),
            (21, ["Rain within 12 hrs", "Cloud + Sunny", "Snow within 12hrs"], None),
            (22, ["Cloudy", "Cloud + Sunny", "Snow within 12hrs"], None),
            (
                23,
                ["Rain within 12 hrs", "Cloudy", "Cloud + Sunny", "Snow within 12hrs"],
                None,
            ),
            (24, ["Sunny", "Snow within 12hrs"], None),
            (25, ["Rain within 12 hrs", "Sunny", "Snow within 12hrs"], None),
            (26, ["Cloudy", "Sunny", "Snow within 12hrs"], None),
            (27, ["Rain within 12 hrs", "Cloudy", "Sunny", "Snow within 12hrs"], None),
            (28, ["Cloud + Sunny", "Sunny", "Snow within 12hrs"], None),
            (
                29,
                ["Rain within 12 hrs", "Cloud + Sunny", "Sunny", "Snow within 12hrs"],
                None,
            ),
            (30, ["Cloudy", "Cloud + Sunny", "Sunny", "Snow within 12hrs"], None),
            (
                31,
                [
                    "Rain within 12 hrs",
                    "Cloudy",
                    "Cloud + Sunny",
                    "Sunny",
                    "Snow within 12hrs",
                ],
                None,
            ),
            (32, None, ValueError),
        ]
        for forecast_icons_value, forecast_icons_texts, exc in t:
            if forecast_icons_texts is not None:
                self.assertEqual(
                    forecast_icons_texts,
                    weatherlink.models._forecast_icons_text(forecast_icons_value),
                    forecast_icons_value,
                )
            elif exc:
                with self.assertRaises(exc):
                    weatherlink.models._forecast_icons_text(forecast_icons_value)

    def test_station_observation_model(self):
        observation = weatherlink.models.StationObservation(
            bar_trend=20,
            barometer=29.93,
            inside_temperature=88.8,
            inside_humidity=13.2,
            outside_temperature=98.3,
            outside_humidity=11.1,
            wind_speed=6,
            ten_min_avg_wind_speed=3,
            wind_direction=189,
            rain_rate=122,
            console_battery_voltage=4.321,
            forecast_icons=24,
            forecast_rule_number=18,
            sunrise=datetime.time(hour=5, minute=34),
            sunset=datetime.time(hour=21, minute=2),
            observation_made_at=datetime.datetime(
                2020, 5, 6, 12, 39, 23, 203, tzinfo=tzlocal()
            ),
            identifier=1234,
        )

        self.assertEqual("S", observation.wind_direction_text())

        self.assertEqual("Rising Slowly", observation.bar_trend_text())

        self.assertEqual(
            ["Sunny", "Snow within 12hrs"], observation.forecast_icons_text()
        )

        self.assertEqual(
            "Mostly clear with little temperature change.", observation.forecast_text()
        )

        self.assertEqual(
            {
                "bar_trend": 20,
                "bar_trend_text": "Rising Slowly",
                "barometer": 29.93,
                "inside_temperature": 88.8,
                "inside_humidity": 13.2,
                "outside_temperature": 98.3,
                "outside_humidity": 11.1,
                "wind_speed": 6,
                "ten_min_avg_wind_speed": 3,
                "wind_direction": 189,
                "wind_direction_text": "S",
                "rain_rate": 122,
                "console_battery_voltage": 4.321,
                "forecast_icons": 24,
                "forecast_icons_text": ["Sunny", "Snow within 12hrs"],
                "forecast_rule_number": 18,
                "forecast_text": "Mostly clear with little temperature change.",
                "sunrise": "05:34:00",
                "sunset": "21:02:00",
                "observation_made_at": datetime.datetime(
                    2020, 5, 6, 12, 39, 23, 203, tzinfo=tzlocal()
                ),
                "identifier": 1234,
            },
            observation.to_dict(),
        )

    def test_validate_record(self):
        weatherlink.models.StationObservation.validate_record(
            record_bitstream=BitStream(self.RECORD_BYTES)
        )

        # 100 bytes
        with self.assertRaises(ValueError):
            weatherlink.models.StationObservation.validate_record(
                record_bitstream=BitStream(self.WRONG_SIZE_BYTES)
            )

        with self.assertRaises(weatherlink.exceptions.BadCRC):
            weatherlink.models.StationObservation.validate_record(
                record_bitstream=BitStream(self.BAD_CRC_BYTES)
            )

    def test_validate_packet_type(self):
        with self.assertRaises(ValueError):
            weatherlink.models.StationObservation.validate_packet_type(
                record_bitstream=BitStream(self.RECORD_BYTES)
            )

        rb = BitStream(self.RECORD_BYTES)
        rb.pos = 32  # Where the packet type lives

        weatherlink.models.StationObservation.validate_packet_type(record_bitstream=rb)

    def test_init_with_bytes(self):
        observation = weatherlink.models.StationObservation.init_with_bytes(
            self.RECORD_BYTES,
            identifier=1234,
            observation_made_at=datetime.datetime(
                2020, 1, 23, 12, 34, 11, tzinfo=tzlocal()
            ),
        )
        self.assertEqual(
            {
                "bar_trend": -60,
                "bar_trend_text": "Falling Rapidly",
                "barometer": 29.41,
                "inside_temperature": 89.4,
                "inside_humidity": 18.0,
                "outside_temperature": 75.5,
                "outside_humidity": 36.0,
                "wind_speed": 5,
                "ten_min_avg_wind_speed": 7,
                "wind_direction": 207,
                "wind_direction_text": "SSW",
                "rain_rate": 0,
                "console_battery_voltage": 4.810546875,
                "forecast_icons": 7,
                "forecast_icons_text": [
                    "Rain within 12 hrs",
                    "Cloudy",
                    "Cloud + Sunny",
                ],
                "forecast_rule_number": 173,
                "forecast_text": "Increasing clouds with little temperature "
                "change. Precipitation possible within 6 hours."
                " Windy with possible wind shift to the W NW or N.",
                "sunrise": "05:35:00",
                "sunset": "20:26:00",
                "observation_made_at": datetime.datetime(
                    2020, 1, 23, 12, 34, 11, tzinfo=tzlocal()
                ),
                "identifier": 1234,
            },
            observation.to_dict(),
        )
