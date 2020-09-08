"""
Pollen Package

Currently is dependent on the BreezoMeter package, but should be
extended to other, hopefully government-sponsored, API sources.
"""
# Supercell Code
from supercell.breezometer.constants import POLLEN_FORECAST_FEATURES
from supercell.breezometer.pollen.models.pollen_collection_api_response import (
    PollenCollectionAPIResponse,
)
from supercell.breezometer.utils import get_current_timestamp, make_api_request


def forecast_daily(
    api_key: str, latitude: float, longitude: float, days: int, **extra_options
) -> PollenCollectionAPIResponse:
    """
    Get a daily forecast of pollen levels in an area.

    :param api_key: The BreezoMeter API key.
    :param latitude: The decimal latitude of the location. Positive values
                     are for the northern hemisphere, and negative for
                     the sourthern.
    :param longitude: The decimal longitude of the location. Positive values
                      are for east of the grenwich meridian, and negative values
                      are for areas to the west.
    :param days: The number of days to receive forecasts for.
    :param extra_options: All additional keyword parameters will be collected
                          and passed as parameters to :meth:`~supercell.breezometer.utils.make_api_request`
                          which can control aspects of the HTTP request.
    :return: A :class:`~supercell.breezometer.pollen.models.pollen_collection_api_response.PollenCollectionAPIResponse`
             object, the
             :attr:`~supercell.breezometer.pollen.models.pollen_collection_api_response.PollenCollectionAPIResponse.data`
             attribute contains a list of
             :class:`~supercell.breezometer.pollen.models.pollen_index_forecast.PollenIndexForecast`
             objects, one for each day request.
    """
    return PollenCollectionAPIResponse.initialize_from_dictionary(
        timestamp=get_current_timestamp(),
        response_dictionary=make_api_request(
            path="/pollen/v2/forecast/daily",
            latitude=latitude,
            longitude=longitude,
            features=POLLEN_FORECAST_FEATURES,
            api_key=api_key,
            metadata=True,
            **extra_options,
        ),
    )
