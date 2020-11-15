# Standard Library
import datetime
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.fires.models.fire_details import FireDetails
from supercell.breezometer.fires.models.fire_details_size import FireDetailsSize


def test_model():
    obj = FireDetails(
        behavior=None,
        cause="Natural",
        name="JESSUP",
        type="Wildfire",
        size=FireDetailsSize(units="m2", value="0.04"),
        status="Final",
        time_discovered=datetime.datetime(2020, 7, 29, 18, 52, 0, tzinfo=tzutc()),
        percent_contained=99.2,
    )
    assert (
        "FireDetails: behavior=None, cause=Natural, name=JESSUP, type=Wildfire, percent_contained=99.2, size=0.04 m2, "
        "status=Final, time_discovered=2020-07-29T18:52:00+00:00"
    ) == str(obj)


def test_model_init_from_dict():
    obj = FireDetails.initialize_from_dictionary(
        response_dictionary={
            "fire_behavior": None,
            "fire_cause": "Natural",
            "fire_name": "JESSUP",
            "fire_type": "Wildfire",
            "percent_contained": 99.2,
            "size": {"units": "m2", "value": 0.04},
            "status": "Final",
            "time_discovered": "2020-07-29T18:52:00Z",
        }
    )
    assert (
        "FireDetails: behavior=None, cause=Natural, name=JESSUP, type=Wildfire, percent_contained=99.2, size=0.04 m2, "
        "status=Final, time_discovered=2020-07-29T18:52:00+00:00"
    ) == str(obj)
