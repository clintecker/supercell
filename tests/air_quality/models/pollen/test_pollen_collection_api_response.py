# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.pollen.pollen_collection_api_response import (
    PollenCollectionAPIResponse,
)
from supercell.air_quality.models.pollen.pollen_index import PollenIndex
from supercell.air_quality.models.pollen.pollen_index_forecast import PollenIndexForecast
from supercell.air_quality.models.pollen.pollen_response_metadata import PollenAPIResponseMetadata
from supercell.air_quality.models.pollen.pollen_type import PollenType


def test_model():
    timestamp = datetime.datetime(2019, 7, 1, 0, 0, 0, tzinfo=tzutc())
    timestamp_2 = datetime.datetime(2019, 7, 2, 0, 0, 0, tzinfo=tzutc())
    assert (
        '{"timestamp": "2020-01-01T01:01:01+00:00", "record_count": 2}, "start_timestamp": '
        '"2019-07-01 00:00:00+00:00", "end_timestamp": "2019-07-05 00:00:00+00:00"}'
    ) == str(
        PollenCollectionAPIResponse(
            metadata=PollenAPIResponseMetadata(
                start_timestamp=datetime.datetime(2019, 7, 1, 0, 0, 0, tzinfo=tzutc()),
                end_timestamp=datetime.datetime(2019, 7, 5, 0, 0, 0, tzinfo=tzutc()),
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
            ),
            data=[
                PollenIndexForecast(
                    timestamp=timestamp,
                    short_name="bpi",
                    display_name="BreezoMeter Pollen Index",
                    pollen_types=[
                        PollenType(
                            short_name="grass",
                            display_name="Grass",
                            in_season=True,
                            data_available=True,
                            index=PollenIndex(
                                value=4, category="High", color="#FF0000"
                            ),
                            timestamp=timestamp,
                        ),
                        PollenType(
                            short_name="weed",
                            display_name="Weed",
                            in_season=True,
                            data_available=True,
                            index=PollenIndex(value=1, category="Low", color="#00FF00"),
                            timestamp=timestamp,
                        ),
                        PollenType(
                            short_name="tree",
                            display_name="Tree",
                            in_season=True,
                            data_available=False,
                            index=PollenIndex(value=None, category="None", color=None),
                            timestamp=timestamp,
                        ),
                    ],
                    plants=[
                        PollenType(
                            short_name="oak",
                            display_name="Oak",
                            in_season=False,
                            data_available=False,
                            index=PollenIndex(value=None, category="None", color=None),
                            timestamp=timestamp,
                        )
                    ],
                ),
                PollenIndexForecast(
                    timestamp=timestamp_2,
                    short_name="bpi",
                    display_name="BreezoMeter Pollen Index",
                    pollen_types=[
                        PollenType(
                            short_name="grass",
                            display_name="Grass",
                            in_season=True,
                            data_available=True,
                            index=PollenIndex(
                                value=4, category="High", color="#FF0000"
                            ),
                            timestamp=timestamp_2,
                        ),
                        PollenType(
                            short_name="weed",
                            display_name="Weed",
                            in_season=True,
                            data_available=True,
                            index=PollenIndex(value=1, category="Low", color="#00FF00"),
                            timestamp=timestamp_2,
                        ),
                        PollenType(
                            short_name="tree",
                            display_name="Tree",
                            in_season=True,
                            data_available=False,
                            index=PollenIndex(value=None, category="None", color=None),
                            timestamp=timestamp_2,
                        ),
                    ],
                    plants=[
                        PollenType(
                            short_name="oak",
                            display_name="Oak",
                            in_season=False,
                            data_available=False,
                            index=PollenIndex(value=None, category="None", color=None),
                            timestamp=timestamp_2,
                        )
                    ],
                ),
            ],
            error=None,
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
        )
    )


def test_initialize_from_dictionary():
    assert (
        '{"timestamp": "2020-09-05T00:00:00+00:00", "record_count": 3}, "start_timestamp": '
        '"2020-09-06 00:00:00", "end_timestamp": "2020-09-08 00:00:00"}'
    ) == str(
        PollenCollectionAPIResponse.initialize_from_dictionary(
            timestamp=datetime.datetime(2020, 9, 5, 0, 0, 0, tzinfo=tzutc()),
            response_dictionary={
                "metadata": {
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
                },
                "data": [
                    {
                        "date": "2020-09-06",
                        "index_id": "bpi",
                        "index_display_name": "BreezoMeter Pollen Index",
                        "types": {
                            "grass": {
                                "display_name": "Grass",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 4,
                                    "category": "High",
                                    "color": "#FF8C00",
                                },
                            },
                            "tree": {
                                "display_name": "Tree",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 0,
                                    "category": "None",
                                    "color": None,
                                },
                            },
                            "weed": {
                                "display_name": "Weed",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 3,
                                    "category": "Moderate",
                                    "color": "#FFFF00",
                                },
                            },
                        },
                        "plants": {
                            "graminales": {
                                "display_name": "Graminales",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 4,
                                    "category": "High",
                                    "color": "#FF8C00",
                                },
                            },
                            "juniper": {
                                "display_name": "Juniper",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "elm": {
                                "display_name": "Elm",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 0,
                                    "category": "None",
                                    "color": None,
                                },
                            },
                            "oak": {
                                "display_name": "Oak",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "alder": {
                                "display_name": "Alder",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "pine": {
                                "display_name": "Pine",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "cottonwood": {
                                "display_name": "Cottonwood",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "ragweed": {
                                "display_name": "Ragweed",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 3,
                                    "category": "Moderate",
                                    "color": "#FFFF00",
                                },
                            },
                            "birch": {
                                "display_name": "Birch",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "ash": {
                                "display_name": "Ash",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "maple": {
                                "display_name": "Maple",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                        },
                    },
                    {
                        "date": "2020-09-07",
                        "index_id": "bpi",
                        "index_display_name": "BreezoMeter Pollen Index",
                        "types": {
                            "grass": {
                                "display_name": "Grass",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 4,
                                    "category": "High",
                                    "color": "#FF8C00",
                                },
                            },
                            "tree": {
                                "display_name": "Tree",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 0,
                                    "category": "None",
                                    "color": None,
                                },
                            },
                            "weed": {
                                "display_name": "Weed",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 3,
                                    "category": "Moderate",
                                    "color": "#FFFF00",
                                },
                            },
                        },
                        "plants": {
                            "graminales": {
                                "display_name": "Graminales",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 4,
                                    "category": "High",
                                    "color": "#FF8C00",
                                },
                            },
                            "juniper": {
                                "display_name": "Juniper",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "elm": {
                                "display_name": "Elm",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 0,
                                    "category": "None",
                                    "color": None,
                                },
                            },
                            "oak": {
                                "display_name": "Oak",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "alder": {
                                "display_name": "Alder",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "pine": {
                                "display_name": "Pine",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "cottonwood": {
                                "display_name": "Cottonwood",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "ragweed": {
                                "display_name": "Ragweed",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 3,
                                    "category": "Moderate",
                                    "color": "#FFFF00",
                                },
                            },
                            "birch": {
                                "display_name": "Birch",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "ash": {
                                "display_name": "Ash",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "maple": {
                                "display_name": "Maple",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                        },
                    },
                    {
                        "date": "2020-09-08",
                        "index_id": "bpi",
                        "index_display_name": "BreezoMeter Pollen Index",
                        "types": {
                            "grass": {
                                "display_name": "Grass",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 4,
                                    "category": "High",
                                    "color": "#FF8C00",
                                },
                            },
                            "tree": {
                                "display_name": "Tree",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "weed": {
                                "display_name": "Weed",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 2,
                                    "category": "Low",
                                    "color": "#84CF33",
                                },
                            },
                        },
                        "plants": {
                            "graminales": {
                                "display_name": "Graminales",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 4,
                                    "category": "High",
                                    "color": "#FF8C00",
                                },
                            },
                            "juniper": {
                                "display_name": "Juniper",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "elm": {
                                "display_name": "Elm",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "oak": {
                                "display_name": "Oak",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "alder": {
                                "display_name": "Alder",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "pine": {
                                "display_name": "Pine",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "cottonwood": {
                                "display_name": "Cottonwood",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "ragweed": {
                                "display_name": "Ragweed",
                                "in_season": True,
                                "data_available": True,
                                "index": {
                                    "value": 2,
                                    "category": "Low",
                                    "color": "#84CF33",
                                },
                            },
                            "birch": {
                                "display_name": "Birch",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "ash": {
                                "display_name": "Ash",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                            "maple": {
                                "display_name": "Maple",
                                "in_season": False,
                                "data_available": False,
                                "index": {
                                    "value": None,
                                    "category": None,
                                    "color": None,
                                },
                            },
                        },
                    },
                ],
                "error": None,
            },
        )
    )
