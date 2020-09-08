# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.air_quality.models.air_quality_index import AirQualityIndex


def test_model():
    assert (
        "AirQualityIndex [2020-01-01T01:01:01+00:00]: AQI (US) = 54 (Moderate air quality) !pm25"
        == str(
            AirQualityIndex(
                short_name="usa_epa",
                display_name="AQI (US)",
                aqi=54,
                aqi_display="54",
                color="#FFFF00",
                category="Moderate air quality",
                dominant_pollutant="pm25",
                timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            )
        )
    )


def test_init_from_dict():
    assert (
        "AirQualityIndex [2020-01-01T01:01:01+00:00]: AQI (US) = 54 (Moderate air quality) !pm25"
        == str(
            AirQualityIndex.initialize_from_dictionary(
                short_name="usa_epa",
                timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                response_dictionary={
                    "display_name": "AQI (US)",
                    "aqi": 54,
                    "aqi_display": "54",
                    "color": "#FFFF00",
                    "category": "Moderate air quality",
                    "dominant_pollutant": "pm25",
                },
            )
        )
    )
