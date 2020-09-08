# Standard Library
from typing import Any, Dict

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterBaseModel


class PollenIndex(BreezoMeterBaseModel):
    value: int
    category: str
    color: str

    def __init__(self, value: int, category: str, color: str) -> None:
        self.value = value
        self.category = category
        self.color = color

    def to_str(self) -> str:
        return '{{"value": {value}, "category": "{category}", "color": "{color}"}}'.format(
            value=self.value, category=self.category, color=self.color
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            value=response_dictionary["value"],
            category=response_dictionary["category"],
            color=response_dictionary["color"],
        )
