# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.air_quality_index import AirQualityIndex
from supercell.air_quality.models.air_quality_pollutant import AirQualityPollutant


def test_model():
    assert (
        "AirQualityPollutant [2020-01-01 01:01:01+00:00]: CO concentration @ "
        "{'value': 124.14, 'units': 'ppb'} - [AirQualityIndex [2020-01-01T01:01:01+00:00]: "
        "Breezometer AQI = 99 (Execellent air quality) !None]"
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
                    display_name="Breezometer AQI",
                    aqi=99,
                    aqi_display="99",
                    color="#009E3A",
                    category="Execellent air quality",
                    timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                )
            ],
        )
    )
