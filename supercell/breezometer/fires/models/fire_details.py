# Standard Library
import datetime
from typing import Any, Dict, Union

# Third Party Code
from dateutil.parser import parse

# Supercell Code
from supercell.breezometer.fires.models.fire_details_size import FireDetailsSize
from supercell.breezometer.models.base import BreezoMeterBaseModel


class FireDetails(BreezoMeterBaseModel):
    behavior: Union[None, str]
    cause: str
    name: str
    type: str
    size: FireDetailsSize
    status: str
    time_discovered: datetime.datetime
    percent_contained: Union[None, float]

    def __init__(
        self,
        behavior: Union[None, str],
        cause: str,
        name: str,
        type: str,
        size: FireDetailsSize,
        status: str,
        time_discovered: datetime.datetime,
        percent_contained: Union[None, float],
    ):
        self.behavior = behavior
        self.cause = cause
        self.name = name
        self.type = type
        self.size = size
        self.status = status
        self.time_discovered = time_discovered
        self.percent_contained = percent_contained
        super(FireDetails, self).__init__()

    def to_str(self):
        return (
            "FireDetails: behavior={behavior}, cause={cause}, name={name}, "
            "type={type}, percent_contained={percent_contained}, size={size}, "
            "status={status}, time_discovered={time_discovered}"
        ).format(
            behavior=self.behavior,
            cause=self.cause,
            name=self.name,
            type=self.type,
            percent_contained=self.percent_contained,
            size=self.size,
            status=self.status,
            time_discovered=self.time_discovered.isoformat(),
        )

    @classmethod
    def initialize_from_dictionary(cls, response_dictionary: Dict[str, Any]):
        return cls(
            behavior=response_dictionary["fire_behavior"],
            cause=response_dictionary["fire_cause"],
            name=response_dictionary["fire_name"],
            type=response_dictionary["fire_type"],
            percent_contained=response_dictionary["percent_contained"],
            size=FireDetailsSize.initialize_from_dictionary(
                response_dictionary["size"]
            ),
            status=response_dictionary["status"],
            time_discovered=parse(response_dictionary["time_discovered"]),
        )
