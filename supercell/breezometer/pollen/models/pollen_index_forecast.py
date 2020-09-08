# Standard Library
import datetime
from typing import Any, Dict, List, Set

# Third Party Code
from dateutil.parser import parse
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterModel
from supercell.breezometer.pollen.models.pollen_type import PollenType


class PollenIndexForecast(BreezoMeterModel):
    short_name: str
    display_name: str
    pollen_types: List[PollenType]
    plants: List[PollenType]
    timestamp: datetime.datetime

    def __init__(
        self,
        timestamp: datetime.datetime,
        short_name: str,
        display_name: str,
        pollen_types: List[PollenType],
        plants: List[PollenType],
    ) -> None:
        self.short_name = short_name
        self.display_name = display_name
        self.pollen_types = pollen_types
        self.plants = plants
        super().__init__(timestamp=timestamp)

    @property
    def plants_in_season(self) -> Set:
        return {pt for pt in self.plants if pt.in_season}

    @property
    def plants_with_data(self) -> Set:
        return {pt for pt in self.plants if pt.data_available}

    @property
    def pollen_types_in_season(self) -> Set:
        return {pt for pt in self.pollen_types if pt.in_season}

    @property
    def pollen_types_with_data(self) -> Set:
        return {pt for pt in self.pollen_types if pt.data_available}

    @property
    def usable_pollen_types(self) -> List:
        return list(self.pollen_types_in_season.union(self.pollen_types_with_data))

    @property
    def usable_plants(self) -> List:
        return list(self.plants_in_season.union(self.plants_with_data))

    def to_str(self) -> str:
        pollen_type_count = len(self.usable_pollen_types)
        plant_count = len(self.usable_plants)
        return (
            '{{"timestamp": "{timestamp}", "display_name": "{display_name}", '
            '"short_name": "{short_name}", "pollen_type_count": {pollen_type_count}, '
            '"plant_count": {plant_count}}}'
        ).format(
            timestamp=self.timestamp.isoformat(),
            display_name=self.display_name,
            short_name=self.short_name,
            pollen_type_count=pollen_type_count,
            plant_count=plant_count,
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        timestamp = parse(
            response_dictionary["date"],
            default=datetime.datetime(year=1979, month=1, day=1, tzinfo=tzutc()),
        )
        return cls(
            short_name=response_dictionary["index_id"],
            display_name=response_dictionary["index_display_name"],
            pollen_types=[
                PollenType.initialize_from_dictionary(
                    timestamp=timestamp,
                    short_name=short_name,
                    response_dictionary=pollen_type_data,
                )
                for short_name, pollen_type_data in response_dictionary["types"].items()
            ],
            plants=[
                PollenType.initialize_from_dictionary(
                    timestamp=timestamp,
                    short_name=short_name,
                    response_dictionary=pollen_type_data,
                )
                for short_name, pollen_type_data in response_dictionary[
                    "plants"
                ].items()
            ],
            timestamp=timestamp,
        )
