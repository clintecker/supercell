"""Air Quality Collection API Response Model"""
# Standard Library
import datetime
from typing import Any, Dict, List, Optional

# Supercell Code
from supercell.air_quality.models.air_quality_api_response_data import AirQualityAPIResponseData
from supercell.air_quality.models.base import AirQualityModel


class AirQualityCollectionAPIResponse(AirQualityModel):
    """Air Quality Collection API Response"""

    str_fmt = "{class_name} [{timestamp}]: data={data} error={error}"
    timestamp: datetime.datetime
    data: List[AirQualityAPIResponseData]
    error: Optional[Dict] = None

    def __init__(
        self,
        data: List[AirQualityAPIResponseData],
        timestamp: datetime.datetime,
        error: Optional[Dict] = None,
    ):
        self.data = data
        self.error = error
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return self.str_fmt.format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp.isoformat(),
            data=self.data,
            error=self.error,
        )

    @classmethod
    def initialize_from_dictionary(
        cls, timestamp: datetime.datetime, response_dictionary: Dict[str, Any]
    ):
        return cls(
            data=[
                AirQualityAPIResponseData.initialize_from_dictionary(
                    response_dictionary=data
                )
                for data in response_dictionary["data"]
            ],
            error=response_dictionary.get("error"),
            timestamp=timestamp,
        )
