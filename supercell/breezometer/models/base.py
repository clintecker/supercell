# Standard Library
import datetime
from typing import Optional


class BreezoMeterBaseModel(object):
    str_fmt: Optional[str]

    def __init__(self):
        pass

    def to_str(self) -> str:
        return self.__class__.__name__

    @property
    def as_string(self) -> str:
        return self.to_str()

    def __str__(self) -> str:
        return self.as_string

    def __repr__(self) -> str:
        return self.as_string


class BreezoMeterModel(BreezoMeterBaseModel):
    def __init__(self, timestamp: datetime.datetime):
        BreezoMeterBaseModel.__init__(self)
        self.timestamp = timestamp
