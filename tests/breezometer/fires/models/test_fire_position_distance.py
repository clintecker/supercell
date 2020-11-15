# Supercell Code
from supercell.breezometer.fires.models.fire_position_distance import (
    FirePositionDistance,
)


def test_model():
    obj = FirePositionDistance(units="km", value=4.3)
    assert "4.3 km" == str(obj)


def test_model_init_from_dict():
    obj = FirePositionDistance.initialize_from_dictionary(
        response_dictionary={"units": "km", "value": 4.3}
    )
    assert "4.3 km" == str(obj)
