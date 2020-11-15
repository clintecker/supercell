# Standard Library
import os

# Third Party Code
import responses

# Supercell Code
from supercell.breezometer.fires import current_conditions
from supercell.breezometer.fires.models.fires_api_response import FiresAPIResponse


@responses.activate
def test_current_air_quality():
    path = os.path.join(
        os.path.dirname(__file__), "..", "example_responses", "current-fires-1.json"
    )
    responses.add(
        responses.GET,
        "https://api.breezometer.com/fires/v1/current-conditions",
        body=open(path, "r").read(),
        adding_headers={"Content-Type": "application/json",},
        status=200,
    )
    assert isinstance(
        current_conditions(
            latitude=39.3939,
            longitude=-109.10909,
            api_key="aaBBccDD",
            radius=100,
            delay=0,
        ),
        FiresAPIResponse,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        "https://api.breezometer.com/fires/v1/current-conditions?"
        "key=aaBBccDD&lat=39.3939&lon=-109.10909&metadata=true&"
        "radius=100"
    )
