# Supercell Code
from supercell.breezometer.fires.models.fire_details_size import FireDetailsSize


def test_model():
    obj = FireDetailsSize(units="km", value=2.2)
    assert "2.2 km" == str(obj)


def test_model_init_from_dict():
    obj = FireDetailsSize.initialize_from_dictionary(
        response_dictionary={"units": "km", "value": 2.2}
    )
    assert "2.2 km" == str(obj)
