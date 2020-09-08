"""Air Quality Pollutant Model"""
# Standard Library
import datetime
from typing import Dict, List, Optional

# Supercell Code
from supercell.breezometer.air_quality.models.air_quality_index import AirQualityIndex
from supercell.breezometer.models.base import BreezoMeterModel


class AirQualityPollutant(BreezoMeterModel):
    """Air Quality Pollutant"""

    str_fmt = "{class_name} [{timestamp}]: {display_name} concentration @ {concentration} - {aqi_information}"
    timestamp: datetime.datetime
    short_name: str
    display_name: str
    full_name: str
    aqi_information: Optional[List[AirQualityIndex]]
    concentration: Dict

    def __init__(
        self,
        short_name: str,
        display_name: str,
        full_name: str,
        concentration: Dict,
        timestamp: datetime.datetime,
        aqi_information: Optional[List[AirQualityIndex]] = [],
    ) -> None:
        self.short_name = short_name
        self.display_name = display_name
        self.full_name = full_name
        self.aqi_information = aqi_information
        self.concentration = concentration
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return self.str_fmt.format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp,
            display_name=self.display_name,
            concentration=self.concentration,
            aqi_information=self.aqi_information,
        )

    @classmethod
    def initialize_from_dict(
        cls, response_dictionary: Dict, short_name: str, timestamp: datetime.datetime
    ):
        aqi_information_data = response_dictionary.get("aqi_information")
        if aqi_information_data:
            aqi_information = [
                AirQualityIndex.initialize_from_dictionary(
                    short_name=short_name,
                    response_dictionary=index_data,
                    timestamp=timestamp,
                )
                for short_name, index_data in aqi_information_data.items()
            ]
        else:
            aqi_information = []
        return cls(
            timestamp=timestamp,
            short_name=short_name,
            display_name=response_dictionary["display_name"],
            full_name=response_dictionary["full_name"],
            concentration=response_dictionary["concentration"],
            aqi_information=aqi_information,
        )
