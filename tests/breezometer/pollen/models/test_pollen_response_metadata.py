# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.pollen.models.pollen_api_response_metadata import (
    PollenAPIResponseMetadata,
)


def test_model():
    assert (
        'PollenAPIResponseMetadata(start_timestamp="2020-01-01T00:00:00+00:00", '
        'end_timestamp="2020-01-05T00:00:00+00:00")'
    ) == str(
        PollenAPIResponseMetadata(
            start_timestamp=datetime.datetime(2020, 1, 1, 0, 0, 0, tzinfo=tzutc()),
            end_timestamp=datetime.datetime(2020, 1, 5, 0, 0, 0, tzinfo=tzutc()),
            location={"country": "United States"},
            types={
                "grass": {"plants": ["graminales"]},
                "tree": {
                    "plants": [
                        "juniper",
                        "elm",
                        "oak",
                        "alder",
                        "pine",
                        "cottonwood",
                        "birch",
                        "ash",
                        "maple",
                    ]
                },
                "weed": {"plants": ["ragweed"]},
            },
        )
    )


def test_initialize_with_dictionary():
    assert (
        'PollenAPIResponseMetadata(start_timestamp="2020-09-06T00:00:00", '
        'end_timestamp="2020-09-08T00:00:00")'
    ) == str(
        PollenAPIResponseMetadata.initialize_from_dictionary(
            response_dictionary={
                "start_date": "2020-09-06",
                "end_date": "2020-09-08",
                "location": {"country": "United States"},
                "types": {
                    "grass": {"plants": ["graminales"]},
                    "tree": {
                        "plants": [
                            "juniper",
                            "elm",
                            "oak",
                            "alder",
                            "pine",
                            "cottonwood",
                            "birch",
                            "ash",
                            "maple",
                        ]
                    },
                    "weed": {"plants": ["ragweed"]},
                },
            }
        )
    )
