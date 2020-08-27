# Standard Library
import datetime
from typing import Any, Dict, List

# Third Party Code
from dateutil.parser import parse


class APIResponseMetadata(object):
    timestamp: datetime.datetime
    location: Dict[str, str]
    indexes: Dict[str, Dict[str, List[str]]]

    def __init__(
        self,
        timestamp: datetime.datetime,
        location: Dict[str, str],
        indexes: Dict[str, Dict[str, List[str]]],
    ) -> None:
        self.timestamp = timestamp
        self.location = location
        self.indexes = indexes

    def __repr__(self) -> str:
        return f"APIResponseMetadata(timestamp='{self.timestamp.isoformat()}', location={self.location})"

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            timestamp=parse(response_dictionary["timestamp"]),
            location=response_dictionary["location"],
            indexes=response_dictionary["indexes"],
        )
