# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.air_quality_api_response_data import AirQualityAPIResponseData
from supercell.air_quality.models.air_quality_index import AirQualityIndex
from supercell.air_quality.models.air_quality_pollutant import AirQualityPollutant


def test_model():
    assert (
        "AirQualityAPIResponseData [2020-01-01 01:01:01.000001+00:00]: data_available=True "
        "indexes=[AirQualityIndex [2020-01-01T01:01:01+00:00]: BreezoMeter AQI = 62 "
        "(Good air quality) !o3, AirQualityIndex [2020-01-01T01:01:01+00:00]: AQI "
        "(US) = 54 (Moderate air quality) !pm25]"
    ) == str(
        AirQualityAPIResponseData(
            timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, 1, tzinfo=tzutc()),
            data_available=True,
            indexes=[
                AirQualityIndex(
                    short_name="baqi",
                    display_name="BreezoMeter AQI",
                    aqi=62,
                    aqi_display="62",
                    color="#B5E21E",
                    category="Good air quality",
                    dominant_pollutant="o3",
                    timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                ),
                AirQualityIndex(
                    short_name="usa_epa",
                    display_name="AQI (US)",
                    aqi=54,
                    aqi_display="54",
                    color="#FFFF00",
                    category="Moderate air quality",
                    dominant_pollutant="pm25",
                    timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                ),
            ],
            pollutants=[
                AirQualityPollutant(
                    display_name="Carbon monoxide",
                    short_name="co",
                    full_name="CO",
                    aqi_information=[
                        AirQualityIndex(
                            short_name="baqi",
                            display_name="BreezoMeter AQI",
                            aqi=98,
                            aqi_display="98",
                            color="#009E3A",
                            category="Excellent air quality",
                            timestamp=datetime.datetime(
                                2020, 1, 1, 1, 1, 1, tzinfo=tzutc()
                            ),
                        )
                    ],
                    concentration={"value": 238.69, "units": "ppb"},
                    timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()),
                )
            ],
        )
    )


def test_initialize_from_dictionary():
    assert (
        "AirQualityAPIResponseData [2020-08-27 17:00:00+00:00]: data_available=True "
        "indexes=[AirQualityIndex [2020-08-27T17:00:00+00:00]: BreezoMeter "
        "AQI = 62 (Good air quality) !o3, AirQualityIndex [2020-08-27T17:00:00+00:00]: "
        "AQI (US) = 54 (Moderate air quality) !pm25]"
    ) == str(
        AirQualityAPIResponseData.initialize_from_dictionary(
            response_dictionary={
                "datetime": "2020-08-27T17:00:00Z",
                "data_available": True,
                "indexes": {
                    "baqi": {
                        "display_name": "BreezoMeter AQI",
                        "aqi": 62,
                        "aqi_display": "62",
                        "color": "#B5E21E",
                        "category": "Good air quality",
                        "dominant_pollutant": "o3",
                    },
                    "usa_epa": {
                        "display_name": "AQI (US)",
                        "aqi": 54,
                        "aqi_display": "54",
                        "color": "#FFFF00",
                        "category": "Moderate air quality",
                        "dominant_pollutant": "pm25",
                    },
                },
                "pollutants": {
                    "co": {
                        "display_name": "CO",
                        "full_name": "Carbon monoxide",
                        "aqi_information": {
                            "baqi": {
                                "display_name": "BreezoMeter AQI",
                                "aqi": 98,
                                "aqi_display": "98",
                                "color": "#009E3A",
                                "category": "Excellent air quality",
                            }
                        },
                        "concentration": {"value": 238.69, "units": "ppb"},
                    },
                    "no2": {
                        "display_name": "NO2",
                        "full_name": "Nitrogen dioxide",
                        "aqi_information": {
                            "baqi": {
                                "display_name": "BreezoMeter AQI",
                                "aqi": 90,
                                "aqi_display": "90",
                                "color": "#009E3A",
                                "category": "Excellent air quality",
                            }
                        },
                        "concentration": {"value": 13.48, "units": "ppb"},
                    },
                    "o3": {
                        "display_name": "O3",
                        "full_name": "Ozone",
                        "aqi_information": {
                            "baqi": {
                                "display_name": "BreezoMeter AQI",
                                "aqi": 62,
                                "aqi_display": "62",
                                "color": "#84CF33",
                                "category": "Good air quality",
                            }
                        },
                        "concentration": {"value": 48.15, "units": "ppb"},
                    },
                    "pm10": {
                        "display_name": "PM10",
                        "full_name": "Inhalable particulate matter (<10\u00b5m)",
                        "aqi_information": {
                            "baqi": {
                                "display_name": "BreezoMeter AQI",
                                "aqi": 74,
                                "aqi_display": "74",
                                "color": "#84CF33",
                                "category": "Good air quality",
                            }
                        },
                        "concentration": {"value": 29.29, "units": "ug/m3"},
                    },
                    "pm25": {
                        "display_name": "PM2.5",
                        "full_name": "Fine particulate matter (<2.5\u00b5m)",
                        "aqi_information": {
                            "baqi": {
                                "display_name": "BreezoMeter AQI",
                                "aqi": 82,
                                "aqi_display": "82",
                                "color": "#009E3A",
                                "category": "Excellent air quality",
                            }
                        },
                        "concentration": {"value": 11.02, "units": "ug/m3"},
                    },
                    "so2": {
                        "display_name": "SO2",
                        "full_name": "Sulfur dioxide",
                        "aqi_information": {
                            "baqi": {
                                "display_name": "BreezoMeter AQI",
                                "aqi": 100,
                                "aqi_display": "100",
                                "color": "#009E3A",
                                "category": "Excellent air quality",
                            }
                        },
                        "concentration": {"value": 0.27, "units": "ppb"},
                    },
                },
            }
        )
    )


def test_initialize_from_dictionary_no_pollutants():
    assert (
        "AirQualityAPIResponseData [2020-08-27 17:00:00+00:00]: data_available=True "
        "indexes=[AirQualityIndex [2020-08-27T17:00:00+00:00]: BreezoMeter "
        "AQI = 62 (Good air quality) !o3, AirQualityIndex [2020-08-27T17:00:00+00:00]: "
        "AQI (US) = 54 (Moderate air quality) !pm25]"
    ) == str(
        AirQualityAPIResponseData.initialize_from_dictionary(
            response_dictionary={
                "datetime": "2020-08-27T17:00:00Z",
                "data_available": True,
                "indexes": {
                    "baqi": {
                        "display_name": "BreezoMeter AQI",
                        "aqi": 62,
                        "aqi_display": "62",
                        "color": "#B5E21E",
                        "category": "Good air quality",
                        "dominant_pollutant": "o3",
                    },
                    "usa_epa": {
                        "display_name": "AQI (US)",
                        "aqi": 54,
                        "aqi_display": "54",
                        "color": "#FFFF00",
                        "category": "Moderate air quality",
                        "dominant_pollutant": "pm25",
                    },
                },
            }
        )
    )
