# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.pollen.pollen_index import PollenIndex
from supercell.air_quality.models.pollen.pollen_type import PollenType


def test_model():
    assert (
        '{"short_name": "grass", "display_name": "Grass", '
        '"in_season": True, "data_available": True, '
        '"index": {"value": 4, "category": "High", "color": '
        '"#FF8C00"}}'
    ) == str(
        PollenType(
            short_name="grass",
            display_name="Grass",
            in_season=True,
            data_available=True,
            index=PollenIndex(value=4, category="High", color="#FF8C00"),
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
        )
    )


def test_initialize_from_dictionary():
    assert (
        '{"short_name": "grass", "display_name": "Grass", '
        '"in_season": True, "data_available": True, '
        '"index": {"value": 4, "category": "High", "color": '
        '"#FF8C00"}}'
    ) == str(
        PollenType.initialize_from_dictionary(
            short_name="grass",
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            response_dictionary={
                "display_name": "Grass",
                "in_season": True,
                "data_available": True,
                "index": {"value": 4, "category": "High", "color": "#FF8C00"},
            },
        )
    )
