"""Air Quality API Response Data Models"""
# Standard Library
import datetime
from typing import Any, Dict, List, Optional

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.air_quality.models.air_quality_index import AirQualityIndex
from supercell.air_quality.models.air_quality_pollutant import AirQualityPollutant
from supercell.air_quality.models.base import AirQualityModel


class AirQualityAPIResponseData(AirQualityModel):
    """Air Quality API Response Data"""

    str_fmt = (
        "{class_name} [{timestamp}]: data_available={data_available} indexes={indexes}"
    )

    timestamp: datetime.datetime
    data_available: bool = False
    indexes: List[AirQualityIndex]
    pollutants: Optional[List[AirQualityPollutant]] = None

    def __init__(
        self,
        timestamp: datetime.datetime,
        data_available: bool,
        indexes: List[AirQualityIndex],
        pollutants: Optional[List[AirQualityPollutant]] = None,
    ) -> None:
        self.indexes = indexes
        self.pollutants = pollutants
        self.data_available = data_available
        super().__init__(timestamp=timestamp)

    def to_str(self) -> str:
        return self.str_fmt.format(
            class_name=self.__class__.__name__,
            timestamp=self.timestamp,
            data_available=self.data_available,
            indexes=self.indexes,
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        timestamp = parse(response_dictionary["datetime"])
        pollutants_data = response_dictionary.get("pollutants")
        if pollutants_data:
            pollutants = [
                AirQualityPollutant.initialize_from_dict(
                    short_name=short_name,
                    response_dictionary=pollutant_data,
                    timestamp=timestamp,
                )
                for short_name, pollutant_data in response_dictionary[
                    "pollutants"
                ].items()
            ]
        else:
            pollutants = []
        return cls(
            timestamp=timestamp,
            indexes=[
                AirQualityIndex.initialize_from_dictionary(
                    short_name=short_name,
                    response_dictionary=index_data,
                    timestamp=timestamp,
                )
                for short_name, index_data in response_dictionary["indexes"].items()
            ],
            pollutants=pollutants,
            data_available=response_dictionary["data_available"],
        )
