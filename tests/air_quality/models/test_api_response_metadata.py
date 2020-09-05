# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.api_response_metadata import APIResponseMetadata


def test_model():
    obj = APIResponseMetadata(
        timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
        location={"country": "United States"},
        indexes={
            "baqi": {"pollutants": ["co", "no2", "o3", "pm10", "pm25", "so2"]},
            "usa_epa": {"pollutants": ["co", "no2", "o3", "pm10", "pm25", "so2"]},
        },
    )
    assert (
        "APIResponseMetadata [2020-01-01T01:01:01+00:00]: location={'country': "
        "'United States'} indexes={'baqi': {'pollutants': ['co', 'no2', 'o3', 'pm10', "
        "'pm25', 'so2']}, 'usa_epa': {'pollutants': ['co', 'no2', 'o3', 'pm10', "
        "'pm25', 'so2']}}"
    ) == str(obj)


def test_model_init_from_dict():
    obj = APIResponseMetadata.initialize_from_dictionary(
        {
            "timestamp": "2020-01-01T01:01:01Z",
            "location": {"country": "United States"},
            "indexes": {
                "baqi": {"pollutants": ["co", "no2", "o3", "pm10", "pm25", "so2"]},
                "usa_epa": {"pollutants": ["co", "no2", "o3", "pm10", "pm25", "so2"]},
            },
        }
    )
    assert (
        "APIResponseMetadata [2020-01-01T01:01:01+00:00]: location={'country': "
        "'United States'} indexes={'baqi': {'pollutants': ['co', 'no2', 'o3', 'pm10', "
        "'pm25', 'so2']}, 'usa_epa': {'pollutants': ['co', 'no2', 'o3', 'pm10', "
        "'pm25', 'so2']}}"
    ) == str(obj)
