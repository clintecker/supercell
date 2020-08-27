# Standard Library
from typing import Dict, Optional

# Supercell Code
from supercell.air_quality.models.air_quality_index import AirQualityIndex


class AirQualityPollutant(object):
    short_name: str
    display_name: str
    full_name: str
    aqi_information: Optional[Dict[str, AirQualityIndex]]
    concentration: Dict

    def __init__(
        self,
        short_name: str,
        display_name: str,
        full_name: str,
        concentration: Dict,
        aqi_information: Optional[Dict[str, AirQualityIndex]] = None,
    ) -> None:
        self.short_name = short_name
        self.display_name = display_name
        self.full_name = full_name
        self.aqi_information = aqi_information
        self.concentration = concentration

    def __repr__(self) -> str:
        return (
            f"AirQualityPollutant(short_name='{self.short_name}', display_name='{self.display_name}', "
            f"full_name='{self.full_name}', aqi_information={self.aqi_information}, concentration={self.concentration})"
        )

    @classmethod
    def initialize_from_dict(cls, response_dictionary: Dict, short_name: str):
        aqi_information_data = response_dictionary.get("aqi_information")
        if aqi_information_data:
            aqi_information = {
                short_name: AirQualityIndex.initialize_from_dictionary(
                    short_name=short_name, response_dictionary=index_data
                )
                for short_name, index_data in aqi_information_data.items()
            }
        else:
            aqi_information = {}
        return cls(
            short_name=short_name,
            display_name=response_dictionary["display_name"],
            full_name=response_dictionary["full_name"],
            concentration=response_dictionary["concentration"],
            aqi_information=aqi_information,
        )
