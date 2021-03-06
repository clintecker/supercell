"""
Air Quality Utilities
"""
# Standard Library
import copy
import datetime
from typing import Any, Dict, Iterable
from urllib.parse import urlunparse

# Third Party Code
from clint_utilities import make_durable_get

API_DOMAIN = "api.breezometer.com"
API_SCHEME = "https"

FAKE_HEADERS = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept-Language": "en-US,en;q=0.5",
}


def build_query_string(
    metadata: bool,
    features: Iterable[str],
    api_key: str,
    longitude: float,
    latitude: float,
    **extra_parameters,
) -> str:
    """Builds an API query string for BreezoMeter"""
    query = extra_parameters
    query.update(
        {
            "metadata": "true" if metadata else "false",
            "key": api_key,
            "lat": latitude,
            "lon": longitude,
        }
    )
    if features:
        query.update({"features": ",".join(features)})

    return "&".join(
        ["{}={}".format(key, value) for key, value in sorted(query.items())]
    )


def build_headers(latitude: float, longitude: float) -> Dict:
    """Builds headers for a request to BreezoMeter"""
    headers = copy.copy(FAKE_HEADERS)
    headers[
        "Referer"
    ] = f"https://breezometer.com/air-quality-map/search?lat={latitude}&lon={longitude}"
    return headers


def build_uri(
    path: str,
    metadata: bool,
    features: Iterable[str],
    api_key: str,
    longitude: float,
    latitude: float,
    **extra_parameters,
) -> str:
    """Builds a full API request URI for BreezoMeter"""
    return urlunparse(
        (
            API_SCHEME,
            API_DOMAIN,
            path,
            None,
            build_query_string(
                metadata=metadata,
                features=features,
                api_key=api_key,
                longitude=longitude,
                latitude=latitude,
                **extra_parameters,
            ),
            None,
        )
    )


def make_api_request(
    path: str,
    latitude: float,
    longitude: float,
    features: Iterable[str],
    api_key: str,
    metadata: bool,
    **extra_parameters,
) -> Dict[str, Any]:
    """Makes an API request to BreezoMeter."""
    # TODO: Add support to `make_durable_get` to support setting headers.
    delay = extra_parameters.pop("delay", 2)
    num_attempts = extra_parameters.pop("num_attempts", 3)
    return make_durable_get(
        build_uri(
            path=path,
            metadata=metadata,
            features=features,
            api_key=api_key,
            longitude=longitude,
            latitude=latitude,
            **extra_parameters,
        ),
        num_attempts=num_attempts,
        delay=delay,
    ).json()


def get_current_timestamp():
    return datetime.datetime.utcnow()
