# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.fires.models.fire import Fire
from supercell.breezometer.fires.models.fire_details import FireDetails
from supercell.breezometer.fires.models.fire_details_size import FireDetailsSize
from supercell.breezometer.fires.models.fire_position import FirePosition
from supercell.breezometer.fires.models.fire_position_distance import (
    FirePositionDistance,
)


def test_model():
    obj = Fire(
        confidence=None,
        details=FireDetails(
            behavior=None,
            cause="Natural",
            name="JESSUP",
            type="Wildfire",
            size=FireDetailsSize(units="m2", value="0.04"),
            status="Final",
            time_discovered=datetime.datetime(2020, 7, 29, 18, 52, 0, tzinfo=tzutc()),
            percent_contained=99.2,
        ),
        position=FirePosition(
            distance=FirePositionDistance(units="km", value=4.3),
            direction=240,
            latitude=39.3939,
            longitude=-104.10410,
        ),
        source="Local Authority",
        update_time=datetime.datetime(2020, 9, 11, 15, 49, 8, tzinfo=tzutc()),
        timestamp=datetime.datetime(2020, 11, 11, 23, 12, 43, tzinfo=tzutc()),
    )
    assert (
        "Fire: details=FireDetails: behavior=None, cause=Natural, name=JESSUP, "
        "type=Wildfire, percent_contained=99.2, size=0.04 m2, status=Final, "
        "time_discovered=2020-07-29T18:52:00+00:00, position=direction=240, "
        "distance=4.3 km, latitude=39.3939, longitude=-104.1041, source=Local "
        "Authority, update_time=2020-09-11T15:49:08+00:00, "
        "timestamp=2020-11-11T23:12:43+00:00"
    ) == str(obj)


def test_model_init_from_dict():
    obj = Fire.initialize_from_dictionary(
        timestamp=datetime.datetime(2020, 11, 11, 23, 12, 43, tzinfo=tzutc()),
        response_dictionary={
            "confidence": None,
            "details": {
                "fire_behavior": None,
                "fire_cause": "Unknown",
                "fire_name": "MM 20",
                "fire_type": "Wildfire",
                "percent_contained": None,
                "size": {"units": "m2", "value": 0.04},
                "status": "Active",
                "time_discovered": "2020-09-06T20:47:00Z",
            },
            "position": {
                "direction": 130,
                "distance": {"units": "km", "value": 40.99},
                "lat": 39.15694,
                "lon": -108.7448,
            },
            "source": "Local Authority",
            "update_time": "2020-09-09T17:38:41Z",
        },
    )
    assert (
        "Fire: details=FireDetails: behavior=None, cause=Unknown, name=MM 20, "
        "type=Wildfire, percent_contained=None, size=0.04 m2, status=Active, "
        "time_discovered=2020-09-06T20:47:00+00:00, position=direction=130, "
        "distance=40.99 km, latitude=39.15694, longitude=-108.7448, source=Local "
        "Authority, update_time=2020-09-09T17:38:41+00:00, "
        "timestamp=2020-11-11T23:12:43+00:00"
    ) == str(obj)
