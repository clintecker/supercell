"""
Air Quality Stuff!

TODO: Other endpoints
- /pollen/v2/current-conditions - No docs
- /pollen/v2/forecast/daily - https://docs.breezometer.com/api-documentation/pollen-api/v2/#daily-forecast
- /v1/weather/currentconditions - https://docs.breezometer.com/weather-api/v1/#current-conditions
  - `/weather/v1/current-conditions` ??
  - "Returns current weather conditions for a specific location"
- /v1/weather/hourlyforecast - https://docs.breezometer.com/weather-api/v1/#hourly-forecast
  - `/weather/v1/forecast/hourly` ??
  - "Returns hourly weather forecasts for the specified location. Each forecast includes hourly weather temperature,
        wind speeds, humidity, precipitation, etc. For a maximum of 120 hours (5 days)."
- /v1/weather/dailyforecast - https://docs.breezometer.com/api-documentation/weather-api/v1/#daily-forecast
  - `/weather/v1/forecast/daily` ??
  - "Each forecast includes daily UV radiation, sunrise and sunset times, and moon conditions for a maximum of
        five days of daily forecasts."
- /fires/v1/current-conditions - https://docs.breezometer.com/api-documentation/fires-api/v1/#current-conditions
"""
# Standard Library
import datetime
import logging

# Supercell Code
from supercell.air_quality.models.air_quality_api_response import AirQualityAPIResponse
from supercell.air_quality.models.air_quality_collection_api_response import (
    AirQualityCollectionAPIResponse,
)
from supercell.air_quality.utils import make_api_request
from supercell.air_quality.constants import (
    AIR_QUALITY_API_FEATURES,
    HISTORICAL_AIR_QUALITY_API_FEATURES,
)

logger = logging.getLogger(__name__)


def current_air_quality(
    latitude: float, longitude: float, api_key: str
) -> AirQualityAPIResponse:
    """Obtain the current air quality information for a specific location"""
    return AirQualityAPIResponse.initialize_from_dictionary(
        response_dictionary=make_api_request(
            path="/air-quality/v2/current-conditions",
            latitude=latitude,
            longitude=longitude,
            features=AIR_QUALITY_API_FEATURES,
            api_key=api_key,
            metadata=True,
        )
    )


def historical_air_quality_hourly(
    latitude: float, longitude: float, utc_datetime: datetime.datetime, api_key: str
) -> AirQualityAPIResponse:
    """Obtain the historical air quality information for a specific location"""
    return AirQualityAPIResponse.initialize_from_dictionary(
        response_dictionary=make_api_request(
            path="/air-quality/v2/historical/hourly",
            latitude=latitude,
            longitude=longitude,
            features=HISTORICAL_AIR_QUALITY_API_FEATURES,
            api_key=api_key,
            metadata=True,
            datetime=utc_datetime.isoformat(),
        )
    )


def air_quality_forecast_hourly(
    latitude: float, longitude: float, hours: int, api_key: str
) -> AirQualityCollectionAPIResponse:
    """Obtain hourly air quality forecasts for a specific location"""
    return AirQualityCollectionAPIResponse.initialize_from_dictionary(
        response_dictionary=make_api_request(
            path="/air-quality/v2/forecast/hourly",
            latitude=latitude,
            longitude=longitude,
            features=[],
            api_key=api_key,
            metadata=False,  # Could make this true to obtain a list of timestamps
            hours=hours,
        )
    )
