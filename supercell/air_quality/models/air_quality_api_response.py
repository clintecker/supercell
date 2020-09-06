"""Air Quality API Response Model"""
# Standard Library
import datetime
from typing import Any, Dict, Optional

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.air_quality.models.air_quality_api_response_data import AirQualityAPIResponseData
from supercell.air_quality.models.api_response_metadata import APIResponseMetadata
from supercell.air_quality.models.base import AirQualityModel


class AirQualityAPIResponse(AirQualityModel):
    """Air Quality API Response"""

    str_fmt = (
        "{class_name} [{timestamp}]: metadata={metadata} data={data} error={error}"
    )
    timestamp: datetime.datetime
    metadata: Optional[APIResponseMetadata]
    data: AirQualityAPIResponseData
    error: Optional[Dict] = None

    def __init__(
        self,
        data: AirQualityAPIResponseData,
        metadata: Optional[APIResponseMetadata],
        error: Optional[Dict],
        timestamp: datetime.datetime,
    ):
        self.metadata = metadata
        self.data = data
        self.error = error
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return self.str_fmt.format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp.isoformat(),
            metadata=self.metadata,
            data=self.data,
            error=self.error,
        )

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
            timestamp=metadata
            and metadata.timestamp
            or parse(response_dictionary["data"]["datetime"]),
        )
