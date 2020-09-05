"""
Air Quality Stuff!

Currently this is built pretty specifically against an API administered by
"Breezometer" but its perhaps feasible it could be amended to use other
services to get similar information.
"""
# Standard Library
import datetime
import logging

# Supercell Code
from supercell.air_quality.constants import (
    AIR_QUALITY_API_FEATURES,
    HISTORICAL_AIR_QUALITY_API_FEATURES,
)
from supercell.air_quality.models.air_quality_api_response import AirQualityAPIResponse
from supercell.air_quality.models.air_quality_collection_api_response import (
    AirQualityCollectionAPIResponse,
)
from supercell.air_quality.utils import make_api_request

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
        ),
        timestamp=datetime.datetime.utcnow(),
    )
