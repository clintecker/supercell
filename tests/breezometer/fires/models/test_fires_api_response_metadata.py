# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.fires.models.fires_api_response_metadata import (
    FiresAPIResponseMetadata,
)


def test_model():
    obj = FiresAPIResponseMetadata(
        timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
        location={"country": "United States"},
    )
    assert (
        "FiresAPIResponseMetadata [2020-01-01T01:01:01+00:00]: location={'country': "
        "'United States'}"
    ) == str(obj)


def test_model_init_from_dict():
    obj = FiresAPIResponseMetadata.initialize_from_dictionary(
        {"timestamp": "2020-01-01T01:01:01Z", "location": {"country": "United States"},}
    )
    assert (
        "FiresAPIResponseMetadata [2020-01-01T01:01:01+00:00]: location={'country': "
        "'United States'}"
    ) == str(obj)
