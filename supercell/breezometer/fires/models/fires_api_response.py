"""Fires Collection API Response Model"""
# Standard Library
import datetime
from typing import Any, Dict, Optional

# Supercell Code
from supercell.breezometer.fires.models.fires_api_response_data import (
    FiresAPIResponseData,
)
from supercell.breezometer.fires.models.fires_api_response_metadata import (
    FiresAPIResponseMetadata,
)
from supercell.breezometer.models.base import BreezoMeterModel


class FiresAPIResponse(BreezoMeterModel):
    """Fires Collection API Response"""

    str_fmt = "{class_name} [{timestamp}]: data={data} error={error}"
    timestamp: datetime.datetime
    data: FiresAPIResponseData
    error: Optional[Dict] = None
    metadata: FiresAPIResponseMetadata

    def __init__(
        self,
        data: FiresAPIResponseData,
        timestamp: datetime.datetime,
        metadata: FiresAPIResponseMetadata,
        error: Optional[Dict] = None,
    ):
        self.data = data
        self.error = error
        self.metadata = metadata
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return "{class_name} [{timestamp}]: data={data} error={error} metadata={metadata}".format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp,
            data=self.data,
            error=self.error,
            metadata=self.metadata,
        )

    @classmethod
    def initialize_from_dictionary(
        cls, timestamp: datetime.datetime, response_dictionary: Dict[str, Any]
    ):
        return cls(
            data=FiresAPIResponseData.initialize_from_dictionary(
                response_dictionary=response_dictionary["data"]
            ),
            error=response_dictionary.get("error"),
            timestamp=timestamp,
            metadata=FiresAPIResponseMetadata.initialize_from_dictionary(
                response_dictionary=response_dictionary["metadata"],
            ),
        )
