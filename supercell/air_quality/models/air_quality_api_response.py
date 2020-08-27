# Standard Library
from typing import Any, Dict, Optional

# Supercell Code
from supercell.air_quality.models.air_quality_api_response_data import (
    AirQualityAPIResponseData,
)
from supercell.air_quality.models.api_response_metadata import APIResponseMetadata


class AirQualityAPIResponse(object):
    """Air Quality API Response"""

    metadata: Optional[APIResponseMetadata]
    data: AirQualityAPIResponseData
    error: Optional[Dict] = None

    def __init__(
        self,
        data: AirQualityAPIResponseData,
        metadata: Optional[APIResponseMetadata],
        error: Optional[Dict],
    ):
        self.metadata = metadata
        self.data = data
        self.error = error

    def __repr__(self) -> str:
        return f"AirQualityResponse(metadata={self.metadata}, data={self.data}, error={self.error})"

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        """Given a request data dictionary, produce an instance of this class"""
        metadata_data = response_dictionary.get("metadata")
        if metadata_data:
            metadata = APIResponseMetadata.initialize_from_dictionary(
                response_dictionary=response_dictionary["metadata"]
            )
        else:
            metadata = None
        return cls(
            metadata=metadata,
            data=AirQualityAPIResponseData.initialize_from_dictionary(
                response_dictionary=response_dictionary["data"]
            ),
            error=response_dictionary.get("error"),
        )
