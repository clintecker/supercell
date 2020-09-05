"""
API Response Metadata
"""
# Standard Library
import datetime
from typing import Any, Dict, List

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.air_quality.models.base import AirQualityModel


class APIResponseMetadata(AirQualityModel):
    """API Response Metadata Model"""

    str_fmt = "{class_name} [{timestamp}]: location={location} indexes={indexes}"
    timestamp: datetime.datetime
    location: Dict[str, str]
    indexes: Dict[str, Dict[str, List[str]]]

    def __init__(
        self,
        timestamp: datetime.datetime,
        location: Dict[str, str],
        indexes: Dict[str, Dict[str, List[str]]],
    ) -> None:
        self.location = location
        self.indexes = indexes
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return self.str_fmt.format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp.isoformat(),
            location=self.location,
            indexes=self.indexes,
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            timestamp=parse(response_dictionary["timestamp"]),
            location=response_dictionary["location"],
            indexes=response_dictionary["indexes"],
        )
