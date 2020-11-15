# Standard Library
from typing import Any, Dict, Union

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterBaseModel


class FirePositionDistance(BreezoMeterBaseModel):
    units: str
    value: Union[int, float]

    def __init__(self, units: str, value: Union[int, float]) -> None:
        self.units = units
        self.value = value
        super(FirePositionDistance, self).__init__()

    def to_str(self):
        return "{value} {units}".format(value=self.value, units=self.units)

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(**response_dictionary)
