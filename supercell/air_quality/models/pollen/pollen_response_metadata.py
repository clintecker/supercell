# Standard Library
import datetime
from typing import Any, Dict, List

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.air_quality.models.base import AirQualityBaseModel


class PollenAPIResponseMetadata(AirQualityBaseModel):
    """Pollen API Response Metadata Model"""

    start_timestamp: datetime.datetime
    end_timestamp: datetime.datetime
    location: Dict[str, str]
    types: Dict[str, Dict[str, List[str]]]

    def __init__(
        self,
        start_timestamp: datetime.datetime,
        end_timestamp: datetime.datetime,
        location: Dict[str, str],
        types: Dict[str, Dict[str, List[str]]],
    ) -> None:
        self.location = location
        self.types = types
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp

    def to_str(self) -> str:
        return 'PollenAPIResponseMetadata(start_timestamp="{start_timestamp}", end_timestamp="{end_timestamp}")'.format(
            start_timestamp=self.start_timestamp.isoformat(),
            end_timestamp=self.end_timestamp.isoformat(),
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            start_timestamp=parse(response_dictionary["start_date"]),
            end_timestamp=parse(response_dictionary["end_date"]),
            location=response_dictionary["location"],
            types=response_dictionary["types"],
        )
