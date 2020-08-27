# Standard Library
from typing import Any, Dict, Optional


class AirQualityIndex(object):
    display_name: str
    short_name: str
    aqi: int
    aqi_display: str
    color: str
    category: str
    dominant_pollutant: Optional[str] = None

    def __init__(
        self,
        short_name: str,
        display_name: str,
        aqi: int,
        aqi_display: str,
        color: str,
        category: str,
        dominant_pollutant: Optional[str] = None,
    ) -> None:
        self.short_name = short_name
        self.display_name = display_name
        self.aqi = aqi
        self.aqi_display = aqi_display
        self.color = color
        self.category = category
        self.dominant_pollutant = dominant_pollutant

    def __repr__(self) -> str:
        return (
            f"AirQualityIndex(short_name='{self.short_name}', display_name='{self.display_name}', "
            f"aqi='{self.aqi_display}', category='{self.category}', dominant_pollutant='{self.dominant_pollutant}')"
        )

    @classmethod
    def initialize_from_dictionary(
        cls, short_name: str, response_dictionary: Dict[str, Any]
    ):
        return cls(
            short_name=short_name,
            display_name=response_dictionary["display_name"],
            aqi=response_dictionary["aqi"],
            aqi_display=response_dictionary["aqi_display"],
            color=response_dictionary["color"],
            category=response_dictionary["category"],
            dominant_pollutant=response_dictionary.get("dominant_pollutant"),
        )
