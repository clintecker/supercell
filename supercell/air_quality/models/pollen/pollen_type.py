# Standard Library
import datetime
from typing import Any, Dict

# Supercell Code
from supercell.air_quality.models.base import AirQualityModel
from supercell.air_quality.models.pollen.pollen_index import PollenIndex


class PollenType(AirQualityModel):
    short_name: str
    display_name: str
    in_season: bool
    data_available: bool
    index: PollenIndex
    timestamp: datetime.datetime

    def __init__(
        self,
        short_name: str,
        display_name: str,
        in_season: bool,
        data_available: bool,
        index: PollenIndex,
        timestamp: datetime.datetime,
    ) -> None:
        self.short_name = short_name
        self.display_name = display_name
        self.in_season = in_season
        self.data_available = data_available
        self.index = index
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return (
            '{{"short_name": "{short_name}", "display_name": "{display_name}", '
            '"in_season": {in_season}, "data_available": {data_available}, '
            '"index": {index}}}'
        ).format(
            short_name=self.short_name,
            display_name=self.display_name,
            in_season=self.in_season,
            data_available=self.data_available,
            index=self.index,
        )

    @classmethod
    def initialize_from_dictionary(
        cls,
        short_name: str,
        timestamp: datetime.datetime,
        response_dictionary: Dict[str, Any],
    ):
        return cls(
            short_name=short_name,
            display_name=response_dictionary["display_name"],
            in_season=response_dictionary["in_season"],
            data_available=response_dictionary["data_available"],
            index=PollenIndex.initialize_from_dictionary(response_dictionary["index"]),
            timestamp=timestamp,
        )
