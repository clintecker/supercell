# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.pollen.pollen_index import PollenIndex
from supercell.air_quality.models.pollen.pollen_index_forecast import PollenIndexForecast
from supercell.air_quality.models.pollen.pollen_type import PollenType


def test_model():
    timestamp = datetime.datetime(2020, 1, 1, 0, 0, 0, tzinfo=tzutc())
    assert (
        '{"timestamp": "2020-01-01T00:00:00+00:00", "display_name": '
        '"BreezoMeter Pollen Index", "short_name": "bpi", "pollen_type_count": 3, '
        '"plant_count": 3}'
        == str(
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
                        index=PollenIndex(value=4, category="High", color="#FF8C00"),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="tree",
                        display_name="Tree",
                        in_season=True,
                        data_available=True,
                        index=PollenIndex(value=0, category="None", color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="weed",
                        display_name="Weed",
                        in_season=True,
                        data_available=True,
                        index=PollenIndex(
                            value=3, category="Moderate", color="#FFFF00"
                        ),
                        timestamp=timestamp,
                    ),
                ],
                plants=[
                    PollenType(
                        short_name="graminales",
                        display_name="Graminales",
                        in_season=True,
                        data_available=True,
                        index=PollenIndex(value=4, category="High", color="#FF8C00"),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="juniper",
                        display_name="Juniper",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="elm",
                        display_name="Elm",
                        in_season=True,
                        data_available=True,
                        index=PollenIndex(value=0, category="None", color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="oak",
                        display_name="Oak",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="alder",
                        display_name="Alder",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="pine",
                        display_name="Pine",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="cottonwood",
                        display_name="Cottonwood",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="ragweed",
                        display_name="Ragweed",
                        in_season=True,
                        data_available=True,
                        index=PollenIndex(
                            value=3, category="Moderate", color="#FFFF00"
                        ),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="birch",
                        display_name="Birch",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="ash",
                        display_name="Ash",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                    PollenType(
                        short_name="maple",
                        display_name="Maple",
                        in_season=False,
                        data_available=False,
                        index=PollenIndex(value=None, category=None, color=None),
                        timestamp=timestamp,
                    ),
                ],
            )
        )
    )


def test_initialize_with_dictionary():
    assert (
        '{"timestamp": "2020-09-06T00:00:00+00:00", "display_name": '
        '"BreezoMeter Pollen Index", "short_name": "bpi", "pollen_type_count": 3, '
        '"plant_count": 3}'
        == str(
            PollenIndexForecast.initialize_from_dictionary(
                response_dictionary={
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
                            "index": {"value": 0, "category": "None", "color": None},
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
                            "index": {"value": None, "category": None, "color": None},
                        },
                        "elm": {
                            "display_name": "Elm",
                            "in_season": True,
                            "data_available": True,
                            "index": {"value": 0, "category": "None", "color": None},
                        },
                        "oak": {
                            "display_name": "Oak",
                            "in_season": False,
                            "data_available": False,
                            "index": {"value": None, "category": None, "color": None},
                        },
                        "alder": {
                            "display_name": "Alder",
                            "in_season": False,
                            "data_available": False,
                            "index": {"value": None, "category": None, "color": None},
                        },
                        "pine": {
                            "display_name": "Pine",
                            "in_season": False,
                            "data_available": False,
                            "index": {"value": None, "category": None, "color": None},
                        },
                        "cottonwood": {
                            "display_name": "Cottonwood",
                            "in_season": False,
                            "data_available": False,
                            "index": {"value": None, "category": None, "color": None},
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
                            "index": {"value": None, "category": None, "color": None},
                        },
                        "ash": {
                            "display_name": "Ash",
                            "in_season": False,
                            "data_available": False,
                            "index": {"value": None, "category": None, "color": None},
                        },
                        "maple": {
                            "display_name": "Maple",
                            "in_season": False,
                            "data_available": False,
                            "index": {"value": None, "category": None, "color": None},
                        },
                    },
                }
            )
        )
    )
