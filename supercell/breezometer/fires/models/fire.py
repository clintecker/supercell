# Standard Library
import datetime
from typing import Any, Dict

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.breezometer.fires.models.fire_details import FireDetails
from supercell.breezometer.fires.models.fire_position import FirePosition
from supercell.breezometer.models.base import BreezoMeterModel


class Fire(BreezoMeterModel):
    confidence: Any
    details: FireDetails
    position: FirePosition
    source: str
    update_time: datetime.datetime

    def __init__(
        self,
        confidence: Any,
        details: FireDetails,
        position: FirePosition,
        source: str,
        update_time: datetime.datetime,
        timestamp: datetime.datetime,
    ):
        self.confidence = confidence
        self.details = details
        self.position = position
        self.source = source
        self.update_time = update_time

        super(Fire, self).__init__(timestamp=timestamp)

    def to_str(self):
        return (
            "Fire: details={details}, position={position}, source={source}, "
            "update_time={update_time}, timestamp={timestamp}"
        ).format(
            details=self.details,
            position=self.position,
            source=self.source,
            update_time=self.update_time.isoformat(),
            timestamp=self.timestamp.isoformat(),
        )

    @classmethod
    def initialize_from_dictionary(
        cls, timestamp: datetime.datetime, response_dictionary: Dict[str, Any]
    ):
        return cls(
            confidence=response_dictionary["confidence"],
            details=FireDetails.initialize_from_dictionary(
                response_dictionary["details"]
            ),
            position=FirePosition.initialize_from_dictionary(
                response_dictionary["position"]
            ),
            source=response_dictionary["source"],
            update_time=parse(response_dictionary["update_time"]),
            timestamp=timestamp,
        )
