# Standard Library
import datetime
from typing import Any, Dict, Optional

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.air_quality.models.air_quality_index import AirQualityIndex
from supercell.air_quality.models.air_quality_pollutant import AirQualityPollutant


class AirQualityAPIResponseData(object):
    """Air Quality API Response Data"""

    timestamp: datetime.datetime
    data_available: bool = False
    indexes: Dict[str, AirQualityIndex]
    pollutants: Optional[Dict[str, AirQualityPollutant]] = None

    def __init__(
        self,
        timestamp: datetime.datetime,
        data_available: bool,
        indexes: Dict[str, AirQualityIndex],
        pollutants: Optional[Dict[str, AirQualityPollutant]] = None,
    ) -> None:
        self.timestamp = timestamp
        self.indexes = indexes
        self.pollutants = pollutants
        self.data_available = data_available

    def __repr__(self) -> str:
        return (
            f"AirQualityAPIResponseData(timestamp='{self.timestamp.isoformat()}', "
            f"data_available={self.data_available}, "
            f"indexes={self.indexes}, pollutants={self.pollutants})"
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        pollutants_data = response_dictionary.get("pollutants")
        if pollutants_data:
            pollutants = {
                short_name: AirQualityPollutant.initialize_from_dict(
                    short_name=short_name, response_dictionary=pollutant_data
                )
                for short_name, pollutant_data in response_dictionary[
                    "pollutants"
                ].items()
            }
        else:
            pollutants = {}
        return cls(
            timestamp=parse(response_dictionary["datetime"]),
            indexes={
                short_name: AirQualityIndex.initialize_from_dictionary(
                    short_name=short_name, response_dictionary=index_data
                )
                for short_name, index_data in response_dictionary["indexes"].items()
            },
            pollutants=pollutants,
            data_available=response_dictionary["data_available"],
        )
