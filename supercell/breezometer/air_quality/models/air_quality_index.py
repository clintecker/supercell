"""Air Quality Index Model"""
# Standard Library
import datetime
from typing import Any, Dict, Optional

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterModel


class AirQualityIndex(BreezoMeterModel):
    str_fmt = "{class_name} [{timestamp}]: {display_name} = {aqi_display} ({category}) !{dominant_pollutant}"
    short_name: str
    display_name: str
    aqi: int
    aqi_display: str
    color: str
    category: str
    dominant_pollutant: Optional[str] = None
    timestamp: datetime.datetime

    def __init__(
        self,
        short_name: str,
        display_name: str,
        aqi: int,
        aqi_display: str,
        color: str,
        category: str,
        timestamp: datetime.datetime,
        dominant_pollutant: Optional[str] = None,
    ):
        self.short_name = short_name
        self.display_name = display_name
        self.aqi = aqi
        self.aqi_display = aqi_display
        self.color = color
        self.category = category
        self.dominant_pollutant = dominant_pollutant
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return self.str_fmt.format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp.isoformat(),
            display_name=self.display_name,
            aqi_display=self.aqi_display,
            category=self.category,
            dominant_pollutant=self.dominant_pollutant,
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
            timestamp=timestamp,
            display_name=response_dictionary["display_name"],
            aqi=response_dictionary["aqi"],
            aqi_display=response_dictionary["aqi_display"],
            category=response_dictionary["category"],
            color=response_dictionary["color"],
            dominant_pollutant=response_dictionary.get("dominant_pollutant"),
        )
