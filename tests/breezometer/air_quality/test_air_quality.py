# Standard Library
import datetime
import os

# Third Party Code
from dateutil.tz import tzutc
import responses

# Supercell Code
from supercell.breezometer.air_quality import (
    air_quality_forecast_hourly,
    current_air_quality,
    historical_air_quality_hourly,
)
from supercell.breezometer.air_quality.models.air_quality_api_response import (
    AirQualityAPIResponse,
)
from supercell.breezometer.air_quality.models.air_quality_collection_api_response import (
    AirQualityCollectionAPIResponse,
)


@responses.activate
def test_current_air_quality():
    path = os.path.join(
        os.path.dirname(__file__), "..", "example_responses", "current-example-1.json"
    )
    responses.add(
        responses.GET,
        "https://api.breezometer.com/air-quality/v2/current-conditions",
        body=open(path, "r").read(),
        adding_headers={"Content-Type": "application/json",},
        status=200,
    )
    assert isinstance(
        current_air_quality(
            latitude=39.3939, longitude=-109.10909, api_key="aaBBccDD", delay=0,
        ),
        AirQualityAPIResponse,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        "https://api.breezometer.com/air-quality/v2/current-conditions?"
        "features=breezometer_aqi,local_aqi,pollutants_concentrations,"
        "all_pollutants_concentrations,pollutants_aqi_information&"
        "key=aaBBccDD&lat=39.3939&lon=-109.10909&metadata=true"
    )


@responses.activate
def test_air_quality_forecast_hourly():
    path = os.path.join(
        os.path.dirname(__file__), "..", "example_responses", "forecast-example-1.json"
    )
    responses.add(
        responses.GET,
        "https://api.breezometer.com/air-quality/v2/forecast/hourly",
        body=open(path, "r").read(),
        adding_headers={"Content-Type": "application/json",},
        status=200,
    )
    assert isinstance(
        air_quality_forecast_hourly(
            latitude=39.3939,
            longitude=-109.10909,
            api_key="aaBBccDD",
            delay=0,
            hours=120,
        ),
        AirQualityCollectionAPIResponse,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        "https://api.breezometer.com/air-quality/v2/forecast/hourly?"
        "hours=120&key=aaBBccDD&lat=39.3939&lon=-109.10909&metadata=false"
    )


@responses.activate
def test_historical_air_quality_hourly():
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "example_responses",
        "historical-example-1.json",
    )
    responses.add(
        responses.GET,
        "https://api.breezometer.com/air-quality/v2/historical/hourly",
        body=open(path, "r").read(),
        adding_headers={"Content-Type": "application/json",},
        status=200,
    )
    assert isinstance(
        historical_air_quality_hourly(
            latitude=39.3939,
            longitude=-109.10909,
            api_key="aaBBccDD",
            delay=0,
            utc_datetime=datetime.datetime(2020, 8, 24, 18, 16, 22, tzinfo=tzutc()),
        ),
        AirQualityAPIResponse,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        "https://api.breezometer.com/air-quality/v2/historical/hourly?"
        "datetime=2020-08-24T18:16:22+00:00&features=breezometer_aqi&"
        "key=aaBBccDD&lat=39.3939&lon=-109.10909&metadata=true"
    )
