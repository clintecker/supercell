# Supercell Code
from supercell.breezometer.fires.models.fire_position import FirePosition
from supercell.breezometer.fires.models.fire_position_distance import (
    FirePositionDistance,
)


def test_model():
    obj = FirePosition(
        distance=FirePositionDistance(units="km", value=4.3),
        direction=240,
        latitude=39.3939,
        longitude=-104.10410,
    )
    assert (
        "direction=240, distance=4.3 km, latitude=39.3939, longitude=-104.1041"
        == str(obj)
    )


def test_model_init_from_dict():
    obj = FirePosition.initialize_from_dictionary(
        response_dictionary={
            "direction": 240,
            "lat": 39.3939,
            "lon": -104.10410,
            "distance": {"units": "km", "value": 4.3},
        }
    )
    assert (
        "direction=240, distance=4.3 km, latitude=39.3939, longitude=-104.1041"
        == str(obj)
    )
