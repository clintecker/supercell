"""
Fires

Currently this is built pretty specifically against an API administered by
"BreezoMeter" but its perhaps feasible it could be amended to use other
services to get similar information.
"""
# Standard Library
import logging

# Supercell Code
from supercell.breezometer.fires.models.fires_api_response import FiresAPIResponse
from supercell.breezometer.utils import get_current_timestamp, make_api_request

logger = logging.getLogger(__name__)


def current_conditions(
    latitude: float, longitude: float, api_key: str, radius: int, **extra_options
):
    """
    Obtain the fires information for a specific location

    :param latitude: The latitude of the center of the area to search for fires.
    :param longitude: The longitude of the center of the area to search for fires.
    :param api_key: The BreezoMeter API key.
    :param radius: The radius of the area to search for fires.
    """
    return FiresAPIResponse.initialize_from_dictionary(
        timestamp=get_current_timestamp(),
        response_dictionary=make_api_request(
            path="/fires/v1/current-conditions",
            latitude=latitude,
            longitude=longitude,
            api_key=api_key,
            metadata=True,
            features=[],
            radius=radius,
            **extra_options
        ),
    )
