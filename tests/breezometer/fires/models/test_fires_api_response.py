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
from supercell.breezometer.fires.models.fires_api_response import FiresAPIResponse
from supercell.breezometer.fires.models.fires_api_response_data import (
    FiresAPIResponseData,
)
from supercell.breezometer.fires.models.fires_api_response_metadata import (
    FiresAPIResponseMetadata,
)


def test_model():
    obj = str(
        FiresAPIResponse(
            data=FiresAPIResponseData(
                timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                data_available=True,
                fires=[
                    Fire(
                        confidence=None,
                        details=FireDetails(
                            behavior=None,
                            cause="Natural",
                            name="JESSUP",
                            type="Wildfire",
                            size=FireDetailsSize(units="m2", value="0.04"),
                            status="Final",
                            time_discovered=datetime.datetime(
                                2020, 7, 29, 18, 52, 0, tzinfo=tzutc()
                            ),
                            percent_contained=99.2,
                        ),
                        position=FirePosition(
                            distance=FirePositionDistance(units="km", value=4.3),
                            direction=240,
                            latitude=39.3939,
                            longitude=-104.10410,
                        ),
                        source="Local Authority",
                        update_time=datetime.datetime(
                            2020, 9, 11, 15, 49, 8, tzinfo=tzutc()
                        ),
                        timestamp=datetime.datetime(
                            2020, 11, 11, 23, 12, 43, tzinfo=tzutc()
                        ),
                    ),
                    Fire(
                        confidence=None,
                        details=FireDetails(
                            behavior=None,
                            cause="Humanmade",
                            name="MM 10",
                            type="Wildfire",
                            size=FireDetailsSize(units="m2", value="3.13"),
                            status="Final",
                            time_discovered=datetime.datetime(
                                2020, 6, 21, 14, 22, 0, tzinfo=tzutc()
                            ),
                            percent_contained=21.2,
                        ),
                        position=FirePosition(
                            distance=FirePositionDistance(units="km", value=1.3),
                            direction=180,
                            latitude=39.3939,
                            longitude=-104.10410,
                        ),
                        source="Local Authority",
                        update_time=datetime.datetime(
                            2020, 9, 11, 15, 49, 8, tzinfo=tzutc()
                        ),
                        timestamp=datetime.datetime(
                            2020, 11, 11, 23, 12, 43, tzinfo=tzutc()
                        ),
                    ),
                ],
            ),
            metadata=FiresAPIResponseMetadata(
                timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                location={"country": "United States"},
            ),
            error=None,
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
        )
    )
    assert (
        "FiresAPIResponse [2020-01-01 01:01:01+00:00]: data=FiresAPIResponseData [2020-01-01 01:01:01.000001+00:00] "
        "data_available=True, fire_count=2 error=None metadata=FiresAPIResponseMetadata [2020-01-01T01:01:01+00:00]: "
        "location={'country': 'United States'}"
    ) == str(obj)


def test_initialize_from_dictionary():
    obj = str(
        FiresAPIResponse.initialize_from_dictionary(
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            response_dictionary={
                "data": {
                    "data_available": True,
                    "datetime": "2020-09-13T19:00:00Z",
                    "fires": [
                        {
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
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Unknown",
                                "fire_name": "WINTER RIDGE 2 ",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 8.34},
                                "status": "Final",
                                "time_discovered": "2020-08-19T22:51:00Z",
                            },
                            "position": {
                                "direction": 287,
                                "distance": {"units": "km", "value": 44.14},
                                "lat": 39.51054,
                                "lon": -109.5994,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-11T15:49:08Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": "Minimal, Smoldering, Creeping, Single Tree Torching",
                                "fire_cause": "Unknown",
                                "fire_name": "Pine Gulch",
                                "fire_type": "Wildfire",
                                "percent_contained": 95.0,
                                "size": {"units": "m2", "value": 56254.19},
                                "status": "Active",
                                "time_discovered": "2020-07-31T23:16:00Z",
                            },
                            "position": {
                                "direction": 97,
                                "distance": {"units": "km", "value": 50.7},
                                "lat": 39.33621,
                                "lon": -108.5255,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-12T22:49:46Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Unknown",
                                "fire_name": "Leach Creek",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Active",
                                "time_discovered": "2020-06-13T14:08:00Z",
                            },
                            "position": {
                                "direction": 118,
                                "distance": {"units": "km", "value": 55.76},
                                "lat": 39.15623,
                                "lon": -108.5399,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-09T17:55:20Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Unknown > Lightning",
                                "fire_name": "West Bangs",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Final",
                                "time_discovered": "2020-06-25T19:24:00Z",
                            },
                            "position": {
                                "direction": 140,
                                "distance": {"units": "km", "value": 66.81},
                                "lat": 38.93038,
                                "lon": -108.6161,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-09T19:52:47Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Human",
                                "fire_name": "GUARDRAIL",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.3},
                                "status": "Final",
                                "time_discovered": "2020-08-11T20:41:00Z",
                            },
                            "position": {
                                "direction": 25,
                                "distance": {"units": "km", "value": 69.35},
                                "lat": 39.96167,
                                "lon": -108.7721,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:19:26Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": "Minimal, Creeping, Smoldering, Smoldering",
                                "fire_cause": "Natural",
                                "fire_name": "FAWN CREEK",
                                "fire_type": "Wildfire",
                                "percent_contained": 100.0,
                                "size": {"units": "m2", "value": 1305.52},
                                "status": "Final",
                                "time_discovered": "2020-07-13T18:00:00Z",
                            },
                            "position": {
                                "direction": 55,
                                "distance": {"units": "km", "value": 72.05},
                                "lat": 39.76213,
                                "lon": -108.4186,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:28:58Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Natural",
                                "fire_name": "ROCK",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Final",
                                "time_discovered": "2020-08-29T21:05:00Z",
                            },
                            "position": {
                                "direction": 18,
                                "distance": {"units": "km", "value": 72.32},
                                "lat": 40.01201,
                                "lon": -108.8432,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:21:15Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": "Minimal, Smoldering, Creeping, Isolated Torching",
                                "fire_cause": "Natural",
                                "fire_name": "WOLF",
                                "fire_type": "Wildfire",
                                "percent_contained": 100.0,
                                "size": {"units": "m2", "value": 110.88},
                                "status": "Final",
                                "time_discovered": "2020-07-14T17:20:00Z",
                            },
                            "position": {
                                "direction": 46,
                                "distance": {"units": "km", "value": 79.27},
                                "lat": 39.88774,
                                "lon": -108.4422,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:29:32Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Unknown",
                                "fire_name": "Ute ",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.12},
                                "status": "Final",
                                "time_discovered": "2020-08-31T23:24:07Z",
                            },
                            "position": {
                                "direction": 158,
                                "distance": {"units": "km", "value": 86.45},
                                "lat": 38.67345,
                                "lon": -108.7301,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-08T16:36:16Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Natural > Lightning",
                                "fire_name": "306",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Final",
                                "time_discovered": "2020-08-30T23:13:00Z",
                            },
                            "position": {
                                "direction": 92,
                                "distance": {"units": "km", "value": 87.97},
                                "lat": 39.3567,
                                "lon": -108.0893,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-09T18:59:37Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": "Minimal, Smoldering, Smoldering",
                                "fire_cause": "Natural",
                                "fire_name": "STEWART",
                                "fire_type": "Wildfire",
                                "percent_contained": 100.0,
                                "size": {"units": "m2", "value": 85.79},
                                "status": "Final",
                                "time_discovered": "2020-07-13T15:17:00Z",
                            },
                            "position": {
                                "direction": 60,
                                "distance": {"units": "km", "value": 90.17},
                                "lat": 39.79328,
                                "lon": -108.195,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:28:16Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Natural",
                                "fire_name": "SANDSTONE",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Final",
                                "time_discovered": "2020-08-29T21:46:00Z",
                            },
                            "position": {
                                "direction": 56,
                                "distance": {"units": "km", "value": 94.02},
                                "lat": 39.85848,
                                "lon": -108.1936,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:21:57Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Natural",
                                "fire_name": "COLLINS",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Final",
                                "time_discovered": "2020-08-29T22:43:00Z",
                            },
                            "position": {
                                "direction": 58,
                                "distance": {"units": "km", "value": 94.41},
                                "lat": 39.84459,
                                "lon": -108.1767,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:22:41Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Natural",
                                "fire_name": "JESSUP",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.04},
                                "status": "Final",
                                "time_discovered": "2020-07-29T18:52:00Z",
                            },
                            "position": {
                                "direction": 59,
                                "distance": {"units": "km", "value": 94.7},
                                "lat": 39.83199,
                                "lon": -108.1629,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-10T17:18:50Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Human > Other Human Cause",
                                "fire_name": "WHITE",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 2.02},
                                "status": "Final",
                                "time_discovered": "2020-04-28T23:25:00Z",
                            },
                            "position": {
                                "direction": 27,
                                "distance": {"units": "km", "value": 96.73},
                                "lat": 40.17034,
                                "lon": -108.5969,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-13T18:26:11Z",
                        },
                        {
                            "confidence": None,
                            "details": {
                                "fire_behavior": None,
                                "fire_cause": "Human > Equipment",
                                "fire_name": "337 Command",
                                "fire_type": "Wildfire",
                                "percent_contained": None,
                                "size": {"units": "m2", "value": 0.81},
                                "status": "Final",
                                "time_discovered": "2020-06-13T19:15:00Z",
                            },
                            "position": {
                                "direction": 85,
                                "distance": {"units": "km", "value": 97.41},
                                "lat": 39.4668,
                                "lon": -107.9817,
                            },
                            "source": "Local Authority",
                            "update_time": "2020-09-09T18:03:10Z",
                        },
                    ],
                },
                "error": None,
                "metadata": {
                    "location": {"country": "United States"},
                    "timestamp": "2020-09-13T19:36:59Z",
                },
            },
        )
    )
    assert (
        "FiresAPIResponse [2020-01-01 01:01:01.000001+00:00]: data=FiresAPIResponseData [2020-09-13 19:00:00+00:00] "
        "data_available=True, fire_count=17 error=None metadata=FiresAPIResponseMetadata [2020-09-13T19:36:59+00:00]: "
        "location={'country': 'United States'}"
    ) == str(obj)
