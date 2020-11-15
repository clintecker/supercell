"""
Fire API Response Metadata
"""
# Standard Library
import datetime
from typing import Any, Dict

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterModel


class FiresAPIResponseMetadata(BreezoMeterModel):
    """Fires API Response Metadata Model"""

    timestamp: datetime.datetime
    location: Dict[str, str]

    def __init__(self, timestamp: datetime.datetime, location: Dict[str, str],) -> None:
        self.location = location
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return "{class_name} [{timestamp}]: location={location}".format(
            location=self.location,
            timestamp=self.timestamp.isoformat(),
            class_name=self.__class__.__name__,
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            timestamp=parse(response_dictionary["timestamp"]),
            location=response_dictionary["location"],
        )
