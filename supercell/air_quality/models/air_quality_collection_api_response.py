# Standard Library
from typing import Any, Dict, List, Optional

# Supercell Code
from supercell.air_quality.models.air_quality_api_response_data import (
    AirQualityAPIResponseData,
)


class AirQualityCollectionAPIResponse(object):
    """Air Quality Collection API Response"""

    data: List[AirQualityAPIResponseData]
    error: Optional[Dict] = None

    def __init__(
        self, data: List[AirQualityAPIResponseData], error: Optional[Dict],
    ):
        self.data = data
        self.error = error

    def __repr__(self) -> str:
        return f"AirQualityCollectionResponse(data={self.data}, error={self.error})"

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            data=[
                AirQualityAPIResponseData.initialize_from_dictionary(
                    response_dictionary=data
                )
                for data in response_dictionary["data"]
            ],
            error=response_dictionary.get("error"),
        )
