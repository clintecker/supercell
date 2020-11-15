# Standard Library
from typing import Any, Dict

# Supercell Code
from supercell.breezometer.fires.models.fire_position_distance import (
    FirePositionDistance,
)
from supercell.breezometer.models.base import BreezoMeterBaseModel


class FirePosition(BreezoMeterBaseModel):
    direction: int
    distance: FirePositionDistance
    latitude: float
    longitude: float

    def __init__(
        self,
        direction: int,
        distance: FirePositionDistance,
        latitude: float,
        longitude: float,
    ):
        self.direction = direction
        self.distance = distance
        self.latitude = latitude
        self.longitude = longitude
        super(FirePosition, self).__init__()

    def to_str(self):
        return (
            "direction={direction}, distance={distance}, "
            "latitude={latitude}, longitude={longitude}"
        ).format(
            direction=self.direction,
            distance=self.distance,
            latitude=self.latitude,
            longitude=self.longitude,
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            direction=response_dictionary["direction"],
            latitude=response_dictionary["lat"],
            longitude=response_dictionary["lon"],
            distance=FirePositionDistance.initialize_from_dictionary(
                response_dictionary=response_dictionary["distance"]
            ),
        )
