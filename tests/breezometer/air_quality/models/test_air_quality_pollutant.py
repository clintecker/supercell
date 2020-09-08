# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.air_quality.models.air_quality_index import AirQualityIndex
from supercell.breezometer.air_quality.models.air_quality_pollutant import (
    AirQualityPollutant,
)


def test_model():
    assert (
        "AirQualityPollutant [2020-01-01 01:01:01+00:00]: CO concentration @ "
        "{'value': 124.14, 'units': 'ppb'} - [AirQualityIndex [2020-01-01T01:01:01+00:00]: "
        "BreezoMeter AQI = 99 (Excellent air quality) !None]"
    ) == str(
        AirQualityPollutant(
            short_name="co",
            full_name="Carbon monoxide",
            display_name="CO",
            concentration={"value": 124.14, "units": "ppb"},
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            aqi_information=[
                AirQualityIndex(
                    short_name="baqi",
                    display_name="BreezoMeter AQI",
                    aqi=99,
                    aqi_display="99",
                    color="#009E3A",
                    category="Excellent air quality",
                    timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                )
            ],
        )
    )


def test_initialize_from_dictionary():
    assert (
        "AirQualityPollutant [2020-01-01 01:01:01+00:00]: CO concentration @ "
        "{'value': 238.69, 'units': 'ppb'} - [AirQualityIndex [2020-01-01T01:01:01+00:00]: "
        "BreezoMeter AQI = 98 (Excellent air quality) !None]"
    ) == str(
        AirQualityPollutant.initialize_from_dict(
            short_name="co",
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            response_dictionary={
                "display_name": "CO",
                "full_name": "Carbon monoxide",
                "aqi_information": {
                    "baqi": {
                        "display_name": "BreezoMeter AQI",
                        "aqi": 98,
                        "aqi_display": "98",
                        "color": "#009E3A",
                        "category": "Excellent air quality",
                    }
                },
                "concentration": {"value": 238.69, "units": "ppb"},
            },
        )
    )


def test_initialize_from_dictionary_aqi_not_present():
    assert (
        "AirQualityPollutant [2020-01-01 01:01:01+00:00]: CO concentration @ "
        "{'value': 238.69, 'units': 'ppb'} - []"
    ) == str(
        AirQualityPollutant.initialize_from_dict(
            short_name="co",
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            response_dictionary={
                "display_name": "CO",
                "full_name": "Carbon monoxide",
                "concentration": {"value": 238.69, "units": "ppb"},
            },
        )
    )
