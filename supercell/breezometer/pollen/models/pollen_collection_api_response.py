"""
Pollen Collection API Response Models
"""
# Standard Library
import datetime
from typing import Any, Dict, List, Optional

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterModel
from supercell.breezometer.pollen.models.pollen_api_response_metadata import (
    PollenAPIResponseMetadata,
)
from supercell.breezometer.pollen.models.pollen_index_forecast import PollenIndexForecast


class PollenCollectionAPIResponse(BreezoMeterModel):
    """
    Pollen Forecast Collection API Response
    """

    timestamp: datetime.datetime
    metadata: PollenAPIResponseMetadata
    data: List[PollenIndexForecast]
    error: Optional[Dict] = None

    def __init__(
        self,
        metadata: PollenAPIResponseMetadata,
        data: List[PollenIndexForecast],
        timestamp: datetime.datetime,
        error: Optional[Dict] = None,
    ):
        self.metadata = metadata
        self.data = data
        self.error = error
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return (
            '{{"timestamp": "{timestamp}", "record_count": {record_count}}}, '
            '"start_timestamp": "{start_timestamp}", "end_timestamp": "{end_timestamp}"}}'
        ).format(
            timestamp=self.timestamp.isoformat(),
            record_count=len(self.data),
            start_timestamp=self.metadata.start_timestamp,
            end_timestamp=self.metadata.end_timestamp,
        )

    @classmethod
    def initialize_from_dictionary(
        cls, timestamp: datetime.datetime, response_dictionary: Dict[str, Any]
    ):
        return cls(
            data=[
                PollenIndexForecast.initialize_from_dictionary(response_dictionary=data)
                for data in response_dictionary["data"]
            ],
            metadata=PollenAPIResponseMetadata.initialize_from_dictionary(
                response_dictionary=response_dictionary["metadata"]
            ),
            error=response_dictionary.get("error"),
            timestamp=timestamp,
        )
