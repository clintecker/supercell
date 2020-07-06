"""Supercell Highway Conditions Package Tests"""
# Standard Library
import unittest

# Third Party Code
import responses

# Supercell Code
import supercell


class SupercellHighwayConditionsTestSuite(unittest.TestCase):
    @responses.activate
    def test_get_segments(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/speed/getSegments.do",
            json={
                "SpeedDetails": {
                    "Segment": [
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 97.5,
                            "SegmentId": "12245",
                            "SegmentName": "AZZA",
                            "Direction": "N",
                            "EndMileMarker": 99.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 80,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 99.5,
                            "SegmentId": "12345",
                            "SegmentName": "AAAA",
                            "Direction": "N",
                            "EndMileMarker": 101.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 83,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 101.5,
                            "SegmentId": "12346",
                            "SegmentName": "AAAB",
                            "Direction": "N",
                            "EndMileMarker": 105.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 81,
                        },
                        {
                            "RoadName": "qqqq",
                            "StartMileMarker": 101.5,
                            "SegmentId": "13346",
                            "SegmentName": "ZAAB",
                            "Direction": "N",
                            "EndMileMarker": 105.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 75,
                            "AverageSpeed": 76,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 199.5,
                            "SegmentId": "23346",
                            "SegmentName": "ZZAB",
                            "Direction": "N",
                            "EndMileMarker": 205.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 78,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 205.5,
                            "SegmentId": "25346",
                            "SegmentName": "ZXAB",
                            "Direction": "N",
                            "EndMileMarker": 209.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 79,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 99.5,
                            "SegmentId": "12394",
                            "SegmentName": "AZZA",
                            "Direction": "S",
                            "EndMileMarker": 97.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 80,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 99.5,
                            "SegmentId": "12345",
                            "SegmentName": "AAAA",
                            "Direction": "S",
                            "EndMileMarker": 101.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 84,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 105.5,
                            "SegmentId": "12349",
                            "SegmentName": "AAAB",
                            "Direction": "S",
                            "EndMileMarker": 101.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 80,
                        },
                        {
                            "RoadName": "qqqq",
                            "StartMileMarker": 105.5,
                            "SegmentId": "13346",
                            "SegmentName": "ZAAB",
                            "Direction": "S",
                            "EndMileMarker": 101.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 75,
                            "AverageSpeed": 74,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 205.5,
                            "SegmentId": "23336",
                            "SegmentName": "ZZAB",
                            "Direction": "S",
                            "EndMileMarker": 199.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 54,
                        },
                        {
                            "RoadName": "zzzz",
                            "StartMileMarker": 209.5,
                            "SegmentId": "25341",
                            "SegmentName": "ZXAB",
                            "Direction": "S",
                            "EndMileMarker": 205.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 79,
                        },
                    ]
                }
            },
        )
        self.assertEqual(
            {
                "N": [
                    {
                        "direction": "N",
                        "end": 101.5,
                        "id": "12345",
                        "limit": 85,
                        "name": "AAAA",
                        "road_id": "WWWW",
                        "speed": 83,
                        "start": 99.5,
                    },
                    {
                        "direction": "N",
                        "end": 105.5,
                        "id": "12346",
                        "limit": 85,
                        "name": "AAAB",
                        "road_id": "WWWW",
                        "speed": 81,
                        "start": 101.5,
                    },
                    {
                        "direction": "N",
                        "end": 205.5,
                        "id": "23346",
                        "limit": 80,
                        "name": "ZZAB",
                        "road_id": "DDDD",
                        "speed": 78,
                        "start": 199.5,
                    },
                ]
            },
            supercell.highways.conditions.get_segments(
                road_name="zzzz",
                start_mile_marker=100.25,
                end_mile_marker=200.55,
                direction="N",
            ),
        )

        self.assertEqual(
            {
                "N": [
                    {
                        "direction": "N",
                        "end": 101.5,
                        "id": "12345",
                        "limit": 85,
                        "name": "AAAA",
                        "road_id": "WWWW",
                        "speed": 83,
                        "start": 99.5,
                    },
                    {
                        "direction": "N",
                        "end": 105.5,
                        "id": "12346",
                        "limit": 85,
                        "name": "AAAB",
                        "road_id": "WWWW",
                        "speed": 81,
                        "start": 101.5,
                    },
                    {
                        "direction": "N",
                        "end": 205.5,
                        "id": "23346",
                        "limit": 80,
                        "name": "ZZAB",
                        "road_id": "DDDD",
                        "speed": 78,
                        "start": 199.5,
                    },
                ],
                "S": [
                    {
                        "direction": "S",
                        "end": 199.5,
                        "id": "23336",
                        "limit": 80,
                        "name": "ZZAB",
                        "road_id": "DDDD",
                        "speed": 54,
                        "start": 205.5,
                    },
                    {
                        "direction": "S",
                        "end": 101.5,
                        "id": "12349",
                        "limit": 85,
                        "name": "AAAB",
                        "road_id": "WWWW",
                        "speed": 80,
                        "start": 105.5,
                    },
                    {
                        "direction": "S",
                        "end": 101.5,
                        "id": "12345",
                        "limit": 85,
                        "name": "AAAA",
                        "road_id": "WWWW",
                        "speed": 84,
                        "start": 99.5,
                    },
                ],
            },
            supercell.highways.conditions.get_segments(
                road_name="zzzz", start_mile_marker=100.25, end_mile_marker=200.55,
            ),
        )

    @responses.activate
    def test_get_segments_bad_response_code(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/speed/getSegments.do",
            json=None,
            status=500,
        )
        self.assertEqual(
            {},
            supercell.highways.conditions.get_segments(
                road_name="zzzz",
                start_mile_marker=100.25,
                end_mile_marker=200.55,
                direction="N",
            ),
        )

    @responses.activate
    def test_get_conditions(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/roadConditions/getRoadConditions.do",
            json={
                "RoadConditionsDetails": {
                    "WeatherRoute": [
                        {
                            "WeatherRouteId": 100,
                            "RoadName": "GGGG",
                            "EndMileMarker": 215.0,
                            "StartMileMarker": 200.0,
                            "RouteName": "GGGG",
                            "RoadId": 12345,
                            "RoadCondition": "Fire",
                            "IsHazardousCondition": "true",
                        },
                        {
                            "WeatherRouteId": 1,
                            "RoadName": "XXXX",
                            "EndMileMarker": 215.0,
                            "StartMileMarker": 200.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Fire",
                            "IsHazardousCondition": "true",
                        },
                        {
                            "WeatherRouteId": 2,
                            "RoadName": "XXXX",
                            "EndMileMarker": 200.0,
                            "StartMileMarker": 150.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Dry",
                            "IsHazardousCondition": "false",
                        },
                        {
                            "WeatherRouteId": 3,
                            "RoadName": "XXXX",
                            "EndMileMarker": 150.0,
                            "StartMileMarker": 125.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Wet",
                            "IsHazardousCondition": "false",
                        },
                        {
                            "WeatherRouteId": 4,
                            "RoadName": "XXXX",
                            "EndMileMarker": 125.0,
                            "StartMileMarker": 101.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Windy",
                            "IsHazardousCondition": "true",
                        },
                        {
                            "WeatherRouteId": 5,
                            "RoadName": "XXXX",
                            "EndMileMarker": 101.0,
                            "StartMileMarker": 95.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Wet",
                            "IsHazardousCondition": "true",
                        },
                    ]
                }
            },
        )

        conditions = supercell.highways.conditions.get_conditions(
            road_name="XXXX", start_mile_marker=100.0, end_mile_marker=199.3
        )

        self.assertEqual(
            [
                {
                    "conditions": "Dry",
                    "end": 200.0,
                    "id": 2,
                    "is_dangerous": False,
                    "name": "XXXX",
                    "road_id": 12345,
                    "start": 150.0,
                },
                {
                    "conditions": "Wet",
                    "end": 150.0,
                    "id": 3,
                    "is_dangerous": False,
                    "name": "XXXX",
                    "road_id": 12345,
                    "start": 125.0,
                },
                {
                    "conditions": "Windy",
                    "end": 125.0,
                    "id": 4,
                    "is_dangerous": True,
                    "name": "XXXX",
                    "road_id": 12345,
                    "start": 101.0,
                },
                {
                    "conditions": "Wet",
                    "end": 101.0,
                    "id": 5,
                    "is_dangerous": True,
                    "name": "XXXX",
                    "road_id": 12345,
                    "start": 95.0,
                },
            ],
            conditions,
        )

    @responses.activate
    def test_get_conditions_bad_status_code(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/roadConditions/getRoadConditions.do",
            json={},
            status=500,
        )
        self.assertEqual(
            [],
            supercell.highways.conditions.get_conditions(
                road_name="XXXX", start_mile_marker=100.0, end_mile_marker=199.3
            ),
        )

    @responses.activate
    def test_get_road_status(self):
        responses.add(
            responses.GET,
            "https://cotrip.org/roadConditions/getRoadConditions.do",
            json={
                "RoadConditionsDetails": {
                    "WeatherRoute": [
                        {
                            "WeatherRouteId": 1,
                            "RoadName": "XXXX",
                            "EndMileMarker": 215.0,
                            "StartMileMarker": 200.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Fire",
                            "IsHazardousCondition": "true",
                        },
                        {
                            "WeatherRouteId": 2,
                            "RoadName": "XXXX",
                            "EndMileMarker": 200.0,
                            "StartMileMarker": 150.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Dry",
                            "IsHazardousCondition": "false",
                        },
                        {
                            "WeatherRouteId": 3,
                            "RoadName": "XXXX",
                            "EndMileMarker": 150.0,
                            "StartMileMarker": 125.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Wet",
                            "IsHazardousCondition": "false",
                        },
                        {
                            "WeatherRouteId": 4,
                            "RoadName": "XXXX",
                            "EndMileMarker": 125.0,
                            "StartMileMarker": 101.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Windy",
                            "IsHazardousCondition": "true",
                        },
                        {
                            "WeatherRouteId": 5,
                            "RoadName": "XXXX",
                            "EndMileMarker": 101.0,
                            "StartMileMarker": 95.0,
                            "RouteName": "XXXX",
                            "RoadId": 12345,
                            "RoadCondition": "Wet",
                            "IsHazardousCondition": "true",
                        },
                    ]
                }
            },
        )
        responses.add(
            responses.GET,
            "https://cotrip.org/speed/getSegments.do",
            json={
                "SpeedDetails": {
                    "Segment": [
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 97.5,
                            "SegmentId": "12245",
                            "SegmentName": "AZZA",
                            "Direction": "N",
                            "EndMileMarker": 99.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 80,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 99.5,
                            "SegmentId": "12345",
                            "SegmentName": "AAAA",
                            "Direction": "N",
                            "EndMileMarker": 101.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 83,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 101.5,
                            "SegmentId": "12346",
                            "SegmentName": "AAAB",
                            "Direction": "N",
                            "EndMileMarker": 105.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 81,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 101.5,
                            "SegmentId": "13346",
                            "SegmentName": "ZAAB",
                            "Direction": "N",
                            "EndMileMarker": 105.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 75,
                            "AverageSpeed": 76,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 199.5,
                            "SegmentId": "23346",
                            "SegmentName": "ZZAB",
                            "Direction": "N",
                            "EndMileMarker": 205.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 78,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 205.5,
                            "SegmentId": "25346",
                            "SegmentName": "ZXAB",
                            "Direction": "N",
                            "EndMileMarker": 209.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 79,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 99.5,
                            "SegmentId": "12394",
                            "SegmentName": "AZZA",
                            "Direction": "S",
                            "EndMileMarker": 97.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 80,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 99.5,
                            "SegmentId": "12345",
                            "SegmentName": "AAAA",
                            "Direction": "S",
                            "EndMileMarker": 101.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 84,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 105.5,
                            "SegmentId": "12349",
                            "SegmentName": "AAAB",
                            "Direction": "S",
                            "EndMileMarker": 101.5,
                            "RoadId": "WWWW",
                            "SpeedLimit": 85,
                            "AverageSpeed": 80,
                        },
                        {
                            "RoadName": "ZZZZ",
                            "StartMileMarker": 105.5,
                            "SegmentId": "13346",
                            "SegmentName": "ZAAB",
                            "Direction": "S",
                            "EndMileMarker": 101.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 75,
                            "AverageSpeed": 74,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 205.5,
                            "SegmentId": "23336",
                            "SegmentName": "ZZAB",
                            "Direction": "S",
                            "EndMileMarker": 199.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 54,
                        },
                        {
                            "RoadName": "XXXX",
                            "StartMileMarker": 209.5,
                            "SegmentId": "25341",
                            "SegmentName": "ZXAB",
                            "Direction": "S",
                            "EndMileMarker": 205.5,
                            "RoadId": "DDDD",
                            "SpeedLimit": 80,
                            "AverageSpeed": 79,
                        },
                    ]
                }
            },
        )
        status = supercell.highways.conditions.get_road_status(
            road_name="XXXX",
            start_mile_marker=100.1,
            end_mile_marker=195.5,
            direction=None,
        )
        self.assertEqual(
            {
                "N": [
                    {
                        "id": "12345",
                        "road_id": "WWWW",
                        "name": "AAAA",
                        "direction": "N",
                        "start": 99.5,
                        "end": 101.5,
                        "limit": 85,
                        "speed": 83,
                        "conditions": "Wet",
                        "is_dangerous": True,
                    },
                    {
                        "id": "12346",
                        "road_id": "WWWW",
                        "name": "AAAB",
                        "direction": "N",
                        "start": 101.5,
                        "end": 105.5,
                        "limit": 85,
                        "speed": 81,
                        "conditions": "Windy",
                        "is_dangerous": True,
                    },
                    {
                        "id": "13346",
                        "road_id": "DDDD",
                        "name": "ZAAB",
                        "direction": "N",
                        "start": 101.5,
                        "end": 105.5,
                        "limit": 75,
                        "speed": 76,
                        "conditions": "Windy",
                        "is_dangerous": True,
                    },
                ],
                "S": [
                    {
                        "id": "12349",
                        "road_id": "WWWW",
                        "name": "AAAB",
                        "direction": "S",
                        "start": 105.5,
                        "end": 101.5,
                        "limit": 85,
                        "speed": 80,
                        "conditions": "Windy",
                        "is_dangerous": True,
                    },
                    {
                        "id": "12345",
                        "road_id": "WWWW",
                        "name": "AAAA",
                        "direction": "S",
                        "start": 99.5,
                        "end": 101.5,
                        "limit": 85,
                        "speed": 84,
                        "conditions": "Wet",
                        "is_dangerous": True,
                    },
                ],
            },
            status,
        )
