# Standard Library
import os

# Third Party Code
import responses

# Supercell Code
from supercell.breezometer.pollen import forecast_daily
from supercell.breezometer.pollen.models.pollen_collection_api_response import (
    PollenCollectionAPIResponse,
)


@responses.activate
def test_forecast_daily():
    path = os.path.join(
        os.path.dirname(__file__), "..", "example_responses", "current-pollen-1.json"
    )
    responses.add(
        responses.GET,
        "https://api.breezometer.com/pollen/v2/forecast/daily",
        body=open(path, "r").read(),
        adding_headers={"Content-Type": "application/json"},
        status=200,
    )
    assert isinstance(
        forecast_daily(
            api_key="aaBBccDD", latitude=39.3939, longitude=-109.109109, days=3, delay=0
        ),
        PollenCollectionAPIResponse,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        "https://api.breezometer.com/pollen/v2/forecast/daily?"
        "features=types_information,plants_information&key=aaBBccDD&"
        "lat=39.3939&lon=-109.109109&metadata=true"
    )
