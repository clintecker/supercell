"""Fires API Response Data Models"""
# Standard Library
import datetime
from typing import Any, Dict, List

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.breezometer.fires.models.fire import Fire
from supercell.breezometer.models.base import BreezoMeterModel


class FiresAPIResponseData(BreezoMeterModel):
    """Fires API Response Data"""

    timestamp: datetime.datetime
    data_available: bool = False
    fires: List[Fire]

    def __init__(
        self, timestamp: datetime.datetime, data_available: bool, fires: List[Fire]
    ) -> None:
        self.data_available = data_available
        self.fires = fires
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return "{class_name} [{timestamp}] data_available={data_available}, fire_count={num_fires}".format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp,
            data_available=self.data_available,
            num_fires=len(self.fires),
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        timestamp = parse(response_dictionary["datetime"])
        fires_data = response_dictionary["fires"]
        fires = [
            Fire.initialize_from_dictionary(
                timestamp=timestamp, response_dictionary=fire_data
            )
            for fire_data in fires_data
        ]
        return cls(
            timestamp=timestamp,
            fires=fires,
            data_available=response_dictionary["data_available"],
        )
